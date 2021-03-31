from django.urls import path
from django.urls.conf import include
from . import views

urlpatterns=[
    # path("monday",views.monday),
    # path("tuesday",views.tuesday),
    # path("wednesday",views.wednesday),
    # path("thursday",views.thursday),
    # path("friday",views.friday),
    # path("satuday",views.saturday),
    # path("sunday",views.sunday),
    path("",views.index), #/challengs
    path("<int:day>",views.monthly_challenge_by_number),
    path("<str:day>",views.monthly_challenges,name="day-challenge"),
    # path("<int:day>",views.monthly_challenge_by_number)

]