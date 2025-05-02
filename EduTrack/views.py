from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import TemplateDoesNotExist, loader
from django.urls import reverse

def homepage(request):
    return render(request, 'index.html')

def pages(request):
    context = {}
    try:

        load_template = request.path.split('/')[-1]

        # if load_template == 'admin':
        #     return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except TemplateDoesNotExist:

        # html_template = loader.get_template('page-404.html')
        # return HttpResponse(html_template.render(context, request))
        pass

    except:
        # html_template = loader.get_template('home/page-500.html')
        # return HttpResponse(html_template.render(context, request))
        pass