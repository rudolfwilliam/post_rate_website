from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def index(request):
    template = 'post/main.html'
    return render(request, template)

