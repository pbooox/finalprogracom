from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pensum/nuevo', views.pensumNuevo, name='pensumNuevo'),
    ]