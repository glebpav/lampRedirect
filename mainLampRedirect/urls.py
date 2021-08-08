from django.contrib import admin
from django.urls import path

from .views import *

urlpatterns = [
    path('l1/on', turn_on_desk_lamp),
    path('l1/off', turn_of_desk_lamp),
]