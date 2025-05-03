from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

# @login_required(login_url="/users/login/")
def homepage(request):
    return render(request, 'index.html')

def pages(request):
    context = {}
    load_template = request.path.split('/')[-1]
    context['segment'] = load_template

    html_template = loader.get_template(load_template)
    return HttpResponse(html_template.render(context, request))