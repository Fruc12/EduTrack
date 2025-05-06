from django.contrib.auth.decorators import login_required, login_not_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

# @login_required(login_url="/accounts/login/")
def homepage(request):
    if request.user.role == "school":
        return redirect('schools:dashboard')
    else:
        return redirect('parents:dashboard')

@login_not_required
def pages(request):
    context = {}
    load_template = request.path.split('/')[-1]
    context['segment'] = load_template

    html_template = loader.get_template(load_template)
    return HttpResponse(html_template.render(context, request))