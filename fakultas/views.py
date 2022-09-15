from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def index(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
def fkip(request):
    template = loader.get_template('fkip.html')
    return HttpResponse(template.render())
def fh(request):
    template = loader.get_template('fh.html')
    return HttpResponse(template.render())
def ft(request):
    template = loader.get_template('ft.html')
    return HttpResponse(template.render())