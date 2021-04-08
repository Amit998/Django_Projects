from django.urls import path


from . import views


urlpatterns=[
    # path("<str:name>",views.index,name="index"),
    path("<int:number>",views.index,name="index"),
    path("",views.home,name="home"),
    path("home/",views.home,name="home"),
    path("create/",views.create,name="Create")

    # path("view/",views.v1,name="view1")
]