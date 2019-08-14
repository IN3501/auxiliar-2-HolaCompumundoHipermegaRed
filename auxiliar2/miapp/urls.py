from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pestaña',views.pestaña, name='pestaña'),
    path('cuerpodocente',views.cuerpodocente, name='cuerpodocente'),
    path('gunsnroses',views.gunsnroses, name='gunsnroses'),
]