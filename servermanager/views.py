from django.shortcuts import render
from servermanager.webdata.identification import identification
# Create your views here.
def index(request):
    return render(request,template_name='index.html')
def post(request):
    if request.method == "POST":
        print(request.FILES)