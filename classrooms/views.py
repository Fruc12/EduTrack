from django.http import Http404
from django.shortcuts import render
from schools.models import School
from .forms import ClassroomForm
from .models import Classroom
from django.shortcuts import get_object_or_404, redirect

def index_classrooms(request, school_pk):
    if request.method == 'POST':
        form = ClassroomForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('schools:classrooms:index', school_pk)
    else:
        form = ClassroomForm()
    school = get_object_or_404(School, pk=school_pk)
    context = {'addForm': form, 'school': school, "classroom" : Classroom()}
    return render(request, "classrooms/classes.html", context)


def delete_classroom(request, school_pk, classroom_pk):
    if request.method == 'POST':
        get_object_or_404(Classroom, pk=classroom_pk).delete()
        return redirect('schools:classrooms:index', school_pk)
    raise Http404(
            "Invalid url."
        )


def show_classroom(request, school_pk, classroom_pk):
    school = get_object_or_404(School, pk=school_pk)
    classroom = get_object_or_404(Classroom, pk=classroom_pk)
    context = {'addForm': None, 'school': school, "classroom" : classroom}
    return render(request, "classrooms/classroom-details.html", context)