from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect, response
from django.urls import reverse

daily_challenges={
    "sunday":"This is sunday",
    "monday":"this is monday",
    "tuesday":"This is tuesday",
    "wednesday":"This is wednesday",
    "thursday":"This is thursday",
    "friday":"This Is Friday",
    "saturday":"This is saturday",
}

# Create your views here.


def index(request):
    list_items=""

    days=list(daily_challenges.keys())

    for day in days:
        capitilize_day=day.capitalize()
        day_path=reverse("day-challenge",args=[day])
        list_items+=f"<li> <a href=\"{day_path}\">{capitilize_day}</a> </li>"



    response_data=f"<ul>{list_items}</ul>"
  
    return HttpResponse(response_data)



# def sunday(request):
#     return HttpResponse("Eat No Meat For Entire month")

# def monday(request):
#     return HttpResponse("Walk For atleast 20 minuts a day")

# def tuesday(request):
#     return HttpResponse("Practice Code for 2 hours")

# def wednesday(request):
#     return HttpResponse("Feed Some poor people or help them")

# def thursday(request):
#     return HttpResponse("Go To College")

# def friday(request):
#     return HttpResponse("Listen New Music")

# def saturday(request):
#     return HttpResponse("Eat Non-veg")

# def sunday(request):
#     return HttpResponse("Eat Healthy Food")

def monthly_challenges(request,day):
    try:
        challenge_text=daily_challenges[day]

        response_data=f"<h1>{day}</h1>"
    except :
        return HttpResponseNotFound("This day is not Found")
    return HttpResponse(response_data)

    # if day == 'sunday':
    #     challenge_text="Eat No Meat For entire day"
    # elif  day=='monday':
    #     challenge_text="Eat Non-veg"
    # else:
    #     return HttpResponseNotFound("This day is not supported")
    # return HttpResponse(challenge_text)

def monthly_challenge_by_number(request,day):
    # try:
    
    forward_day=list(daily_challenges.keys())
    if (day > len(forward_day)  ):
        HttpResponseNotFound("Not Found")
        # challenge_text=daily_challenges[forward_day[day]]
    redirect_day=forward_day[day-1]
    # print("/challenges/",redirect_day)
    # to_url=f"/challenges/{redirect_day}"

    redirect_path=reverse("day-challenge",args=[redirect_day])


    # print(to_url)   
    return HttpResponseRedirect(redirect_path)
    # except :
        # return HttpResponseNotFound("The Day is not Found")
        
    # return HttpResponse(challenge_text)
    # if day == 1:
    #     challenge_text="Day 1"
    # elif  day== 2:
    #     challenge_text="Day 2"
    # else:
    #     return HttpResponseNotFound("This day is not supported")
    # return HttpResponse(challenge_text)

