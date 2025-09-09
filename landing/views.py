from django.shortcuts import render
from django.http import HttpResponse
from datetime import date

# Create your views here.
def home(request):
    today = date.today()
    stack = [{'name': 'Django'}, {'name': 'Python'}, {'name': 'JavaScript'}, {'name': 'HTML'}, {'name': 'CSS'}]
    return render(request, 'landing/landing.html', {
        "name": "Landing Page",
        "date": today,
        "stacks": stack
    })

def stack(request, tool):
    return HttpResponse(f"Estás utilizando la herramienta: {tool}")