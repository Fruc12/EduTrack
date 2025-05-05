from django.shortcuts import render, redirect
from .forms import SchoolForm
from .models import SchoolUser, School
from django.contrib import messages


def dashboard(request):
    context = {}
    return render(request, 'schools/index.html', context)

def index_school(request):
    if request.method == 'POST':
        form = SchoolForm(request.POST)
        if form.is_valid():
            school = form.save()
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


def show_school(request, pk):
    return render(request, "schools/classes.html")


def delete_school(request, pk):
    if request.method == 'POST':
        School.objects.get(pk=pk).delete()
    return redirect('schools:index')
