from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    # return HttpResponse('hello world')
    return render(request, 'project1/home.html')