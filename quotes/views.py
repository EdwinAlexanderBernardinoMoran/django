from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

def days_weeks(request, day):
    quote_text = ''
    if day == 'monday':
        quote_text = "Start your week with positivity!"
    elif day == 'tuesday':
        quote_text = "Keep going, it's only Tuesday!"
    elif day == 'wednesday':
        quote_text = "You're halfway through the week!"
    elif day == 'thursday':
        quote_text = "Almost there, it's Thursday!"
    elif day == 'friday':
        quote_text = "Finish strong, it's Friday!"
    else:
        return HttpResponseNotFound("Invalid day!")

    return HttpResponse(quote_text)
