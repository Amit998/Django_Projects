from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound

# Create your views here.


def sunday(request):
    return HttpResponse("Eat No Meat For Entire month")

def monday(request):
    return HttpResponse("Walk For atleast 20 minuts a day")

def tuesday(request):
    return HttpResponse("Practice Code for 2 hours")

def wednesday(request):
    return HttpResponse("Feed Some poor people or help them")

def thursday(request):
    return HttpResponse("Go To College")

def friday(request):
    return HttpResponse("Listen New Music")

def saturday(request):
    return HttpResponse("Eat Non-veg")

def sunday(request):
    return HttpResponse("Eat Healthy Food")

def monthly_challenges(request,day):

    if day == 'sunday':
        challenge_text="Eat No Meat For entire day"
    elif  day=='monday':
        challenge_text="Eat Non-veg"
    else:
        return HttpResponseNotFound("This day is not supported")
    return HttpResponse(challenge_text)

def monthly_challenge_by_number(request,day):
    return HttpResponse(day)
    # if day == 1:
    #     challenge_text="Day 1"
    # elif  day== 2:
    #     challenge_text="Day 2"
    # else:
    #     return HttpResponseNotFound("This day is not supported")
    # return HttpResponse(challenge_text)

