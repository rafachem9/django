from django.urls import path
from ProyectoWebApp import views
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [

    path('', views.servicios, name= 'Servicios'),

]
