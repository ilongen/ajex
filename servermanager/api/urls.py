from django.urls import path
from api import views

urlpatterns = [
    path('v1/models/RemoveNaN', views.model_RemoveNaN, name='model_RemoveNaN'),
]