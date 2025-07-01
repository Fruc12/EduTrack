import random
import string

from django.contrib.auth.hashers import make_password
from django.core.mail import EmailMessage
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from django.template.loader import render_to_string

from parents.forms import StudentForm, ParentForm
from parents.models import Parent, Student
from schools.models import School, SchoolYear
from users.models import User
from .forms import ClassroomForm, CourseForm, TimeTableForm
from .models import Classroom, Course, TimeTable
from schools.forms import SchoolYearForm
from schools.forms import ChangeYearForm


def index_classrooms(request, school_pk, add_year_form=None):
    if request.method == 'POST':
        form = ClassroomForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('schools:classrooms:index', school_pk)
    else:
        form = ClassroomForm()
    if request.GET.get('school_years'):
        school_year = get_object_or_404(SchoolYear, pk=request.GET.get('school_years'))
    else:
        school_year = get_object_or_404(School, pk=school_pk).schoolYears.order_by('-start_date').first()
    add_year_form = SchoolYearForm() if add_year_form is None else add_year_form
    change_year_form = ChangeYearForm(school_pk=school_pk)
    context = {
        'addForm': form,
        'schoolYear': school_year,
        "classroom" : Classroom(),
        "addYearForm": add_year_form,
        "changeYearForm": change_year_form,
    }
    return render(request, "classrooms/classes.html", context)

def delete_classroom(request, school_pk, classroom_pk):
    if request.method == 'POST':
        get_object_or_404(Classroom, pk=classroom_pk).delete()
        return redirect('schools:classrooms:index', school_pk)
    raise Http404(
            "Invalid url."
        )


def show_classroom(request, school_pk, classroom_pk, course_form=None, time_table_form=None):
    get_object_or_404(School, pk=school_pk)
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    add_student_form = StudentForm()
    add_parent_form = ParentForm()
    courses = classroom.courses.all()
    time_tables = []
    for course in courses:
        for timeTable in course.timeTables.all():
            time_tables.append(timeTable)
    # time_tables.sort()
    print(time_tables)
    context = {
        'addStudentForm': add_student_form,
        'addParentForm': add_parent_form,
        "classroom" : classroom,
        "courseForm": CourseForm() if course_form is None else course_form,
        "timeTableForm": TimeTableForm(classroom_pk=classroom_pk) if time_table_form is None else time_table_form,
        "courses": courses,
        "timeTables": time_tables,
        "DAYS": TimeTable.DAYS

    }
    return render(request, "classrooms/classroom-details.html", context)

def add_student(request, school_pk, classroom_pk):
    if request.method == 'POST':
        add_student_form = StudentForm(request.POST)
        if add_student_form.is_valid():
            add_student_form.save()
            return redirect('schools:classrooms:show', school_pk, classroom_pk)
    else:
        add_student_form = StudentForm()
    add_parent_form = ParentForm()
    context = {
        'addStudentForm': add_student_form,
        'addParentForm': add_parent_form,
        "classroom" : get_object_or_404(Classroom, pk=classroom_pk),
    }
    return render(request, "classrooms/classroom-details.html", context)

def add_parent(request, school_pk, classroom_pk):
    msg = None
    if request.method == 'POST':
        add_parent_form = ParentForm(request.POST)
        if add_parent_form.is_valid():
            user = User(
                first_name=add_parent_form.cleaned_data['first_name'],
                last_name=add_parent_form.cleaned_data['last_name'],
                email=add_parent_form.cleaned_data['email'],
                role = 'parent',
                password = ''.join( random.choices(string.ascii_letters + string.digits, k=10) ),
            )
            parent = Parent(
                phone = add_parent_form.cleaned_data["phone"],
                student = get_object_or_404(Student, pk=request.POST["student"]),
                user = user,
            )
            if register_parent_mailer(parent):
                user.password = make_password(user.password)
                user.is_active = True
                user.save()
                parent.user = user
                parent.save()
                return redirect('schools:classrooms:show', school_pk, classroom_pk)
            msg = "Erreur lors de l'envoi de l'email des identifiants"
        else:
            msg = "Erreur lors de la validation du formulaire"
    else:
        add_parent_form = ParentForm()
    add_student_form = StudentForm()
    context = {
        'addStudentForm': add_student_form,
        'addParentForm': add_parent_form,
        "classroom" : get_object_or_404(Classroom, pk=classroom_pk),
        "msg" : msg,
    }
    return render(request, "classrooms/classroom-details.html", context)

def register_parent_mailer(parent):
    subject = "Identifiants de connexion EduTrack"
    body = render_to_string("mails/register-parent.html", {"parent":parent})
    to = [parent.user.email]
    mail = EmailMessage(subject=subject, body=body, to=to)
    mail.content_subtype = 'html'
    return mail.send()

def add_school_year(request, school_pk):
    if request.method == 'POST':
        form = SchoolYearForm(request.POST)
        if form.is_valid():
            school_year = form.save()
            return redirect('schools:classrooms:index', school_year.school.pk)
        else:
            return index_classrooms(request, request.POST.get('school'), form)
    return redirect('schools:classrooms:index', school_pk)

def add_course(request, school_pk, classroom_pk):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            print("Created")
            return redirect('schools:classrooms:show', school_pk, classroom_pk)
        else:
            return show_classroom(request, school_pk, classroom_pk, course_form=form)
    return redirect('schools:classrooms:show', school_pk, classroom_pk)


def add_time_table(request, school_pk, classroom_pk):
    if request.method == 'POST':
        form = TimeTableForm(request.POST, classroom_pk=classroom_pk)
        if form.is_valid():
            form.save()
            return redirect('schools:classrooms:show', school_pk, classroom_pk)
        else:
            return show_classroom(request, school_pk, classroom_pk, time_table_form=form)
    return redirect('schools:classrooms:show', school_pk, classroom_pk)
