from django.urls import path
from api import views

urlpatterns = [
    path('v1/models/yarth', views.model_yarth),
]