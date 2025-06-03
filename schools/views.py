from django.shortcuts import render, redirect
from django.utils import timezone

from .forms import SchoolForm
from .models import SchoolUser, School, SchoolYear
from django.contrib import messages


def dashboard(request):
    context = {}
    return render(request, 'schools/index.html', context)

def index_school(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            school = form.save()
            SchoolYear(
                school=school,
                start_date=timezone.datetime(day=1, month=9, year=timezone.now().year),
                end_date=timezone.datetime(day=1, month=7, year=timezone.now().year+1),
                name=f"{timezone.now().year}-{timezone.now().year+1}"
            ).save()
            school_user = SchoolUser(
                user = request.user,
                school = school,
                role = 'director'
            )
            school_user.save()
            return redirect('schools:index')
    else:
        form = SchoolForm()
    context = { "addForm" : form }
    return render(request, 'schools/schools.html', context)

def delete_school(request, pk):
    if request.method == 'POST':
        School.objects.get(pk=pk).delete()
    return redirect('schools:index')
