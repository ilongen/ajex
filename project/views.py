from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    template_name = 'index.html'
    return render(request,template_name)

"""
    API: user_data
    modified: 04/05/2025 | 01:31 PM
    describe: This api works on receiving data and preparing for other api/backend services.

"""


def models_ready(request):
    template_name = "models-ready.html"
    return render(request,template_name)