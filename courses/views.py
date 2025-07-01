from django.shortcuts import render, get_object_or_404, redirect

from classrooms.models import Course
from courses.forms import ScoreForm
from courses.models import Score


def index_course(request, course_pk) :
    if request.method == 'POST':
        form = ScoreForm(request.POST)
        if form.is_valid():
            print("Fait")
            score = form.save()
            return redirect('courses:index', course_pk)
        print(form.errors)
    else:
        form = ScoreForm()
    course = get_object_or_404(Course, pk=course_pk);
    context = {
        "scoresI" : course.scores.filter(type='eval'),
        "scoresD" : course.scores.filter(type='exam'),
        "scoreForm": form,
        "course" : course,
    }
    return render(request, 'courses/details-matiere.html', context)

