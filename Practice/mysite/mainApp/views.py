from django.forms import forms
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList,Item
from .forms import CreateNewList



# Create your views here.


# def index(respone,id):
    # return HttpResponse(f"{id}")

# def v1(respone):
    # return HttpResponse("<h1>View One</h1>")

def index(response,number):
    # my_dict-{}
    ls=ToDoList.objects.get(id=number)
    # item=ls.item_set.get(id=1)
    # # item="HI"
    # # print(item)
    # return HttpResponse(f"<h1>{ls.id}</h1><br><p>{item}</p><br>")

    if response.method == "POST":
        print(response.POST)
        if response.POST.get('save'):
            for item in ls.item_set.all():
                if response.POST.get("c"+str(item.id)) == "clicked":
                    item.complete=True
                else:
                    item.complete =False
                item.save()


        elif response.POST.get("newItem"):
            txt=response.POST.get("new")

            if len(txt) >2:
                ls.item_set.create(text=txt,complete=False)
            else:
                print("Invalid Input")
            ls.save()



    return render(response,"mainApp/list.html",{'ls':ls})

def home(response):
    return render(response,"mainApp/home.html",{'name':"Amit"})

def create(response):
    if response.method == "POST":
        form=CreateNewList(response.POST)

        if form.is_valid():
            n=form.cleaned_data["name"]
            t=ToDoList(name=n)
            t.save()
        return HttpResponseRedirect("/%i"%t.id)
    
    else:
        form=CreateNewList()
    return render(response,"mainApp/create.html",{'form':form})