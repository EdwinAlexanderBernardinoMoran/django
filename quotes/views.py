from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

days_of_week = {
    'monday': "Start your week with positivity!",
    'tuesday': "Keep going, it's only Tuesday!",
    'wednesday': "You're halfway through the week!",
    'thursday': "Almost there, it's Thursday!",
    'friday': "Finish strong, it's Friday!"
}

# Create your views here.

def index(request):
    list_items = ""
    days = list(days_of_week.keys())

    for day in days:
        day_path = reverse("day", args=[day])
        list_items += f"<li><a href=\"{day_path}\">{day.title()}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)

def days_weeks_numbers(request, day):
    days = list(days_of_week.keys())

    if day > len(days):
        return HttpResponseNotFound("Invalid day!")
    
    redirect_day = days[day-1]
    redirect_path = reverse("day", args=[redirect_day])
    return HttpResponseRedirect(redirect_path)

def days_weeks(request, day):
    try:
        return HttpResponse(days_of_week[day])
    except KeyError:
        return HttpResponseNotFound("Invalid day!")
