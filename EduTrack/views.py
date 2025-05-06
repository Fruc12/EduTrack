from django.contrib.auth.decorators import login_required, login_not_required
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader

# @login_required(login_url="/accounts/login/")
def homepage(request):
    return redirect('schools:dashboard')
def classe_detail(request, classe_id):
    context = {
        'classe': {
            'nom': 'CM2 A',
            'annee_scolaire': '2023-2024'
        },
        'user': request.user
    }
    return render(request, 'classe_detail.html', context)

@login_not_required
def pages(request):
    context = {}
    load_template = request.path.split('/')[-1]
    context['segment'] = load_template

    html_template = loader.get_template(load_template)
    return HttpResponse(html_template.render(context, request))