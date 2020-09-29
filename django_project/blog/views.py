from django.shortcuts import render
from django.http import  HttpResponse

posts=[
    {
        'author':'Amit',
        'title':'Blog Post 1',
        'content':'First Post Content',
        'date_posted':'12-08-2020'
    },
    {
        'author':'Kuntal',
        'title':'Blog Post 2',
        'content':'Second Post Content',
        'date_posted':'10-02-2020'
    },
    {
        'author':'Ram',
        'title':'Blog Post 3',
        'content':'Third Post Content',
        'date_posted':'02-02-2020'
    },
    {
        'author':'Sam',
        'title':'Blog Post 4',
        'content':'4th Post Content',
        'date_posted':'10-10-2020'
    }
]


def home(request):
    context ={
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About Page'})

# Create your views here.
