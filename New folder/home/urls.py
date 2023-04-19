
from django.contrib import admin
from django.urls import path
from home import views
urlpatterns = [
    path('', views.home),
    path('home', views.home, name='home'),    
    path('excel', views.excel, name='excel'),
    path('about', views.about, name='about'),
    path('remove', views.remove, name='remove'),
    path('setCourceOutcome', views.setCourceOutcome, name='setCourceOutcome'),
    path('setPaper', views.setPaper, name='setPaper'),
    path('displayPaper', views.displayPaper, name='displayPaper'),
    path('capture', views.capture, name='capture'),
    path('storeMarks', views.storeMarks, name='storeMarks'),
]
