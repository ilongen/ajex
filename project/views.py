from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    template_name = 'index.html'
    return render(request,template_name)

def models_ready(request):
    template_name = "models-ready.html"
    return render(request,template_name)


def signin(request):
    template_name = 'sign-in.html'
    return render(request,template_name)


def signup(request):
    template_name = 'sign-up.html'
    return render(request,template_name)

