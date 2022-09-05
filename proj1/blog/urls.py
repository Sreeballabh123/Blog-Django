from django.urls import path
from blog import views

urlpatterns = [
    path('',views.index,name="blog-home"),
    path('about/',views.about, name="blog-about"),
]