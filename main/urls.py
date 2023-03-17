from django.urls import path

from . import views

urlpatterns =[
    path("", views.index, name="index"),
    path("blog", views.blog, name="blog"),
    path("about", views.about, name="about"),
    path('blog/<int:pk>', views.postdetails, name="postdetails"),

]