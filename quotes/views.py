from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello, world!")

def monday(request):
    return HttpResponse("Hello, Monday!")

def tuesday(request):
    return HttpResponse("Hello, Tuesday!")

def wednesday(request):
    return HttpResponse("Hello, Wednesday!")

def thursday(request):
    return HttpResponse("Hello, Thursday!")

def friday(request):
    return HttpResponse("Hello, Friday!")