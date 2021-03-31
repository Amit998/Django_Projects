from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.


def index(respone,id):
    return HttpResponse(f"{id}")

def v1(respone):
    return HttpResponse("<h1>View One</h1>")