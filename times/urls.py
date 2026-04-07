from django.urls import path
from .views import listar_times

urlpatterns = [
    path('', listar_times, name='listar_times'),
]