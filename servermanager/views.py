from django.shortcuts import render
from servermanager.services.DataSheet import DataSheet
from servermanager.services.modelsReady.CleanCell import RemoveNaN
from .forms import postData
# Create your views here.

def index(request):
    template_name = 'index.html'
    return render(request,template_name)

def models_ready(request):
    template_name = "models-ready.html"
    return render(request,template_name)

def postForm(request):
    # Request received from frontend
    if request.method == 'POST':

        # Caso o POST for sucesso, ele irá enviar pro servidor a informação.
        form = postData(request.POST)
        if form.is_valid():
            name_file = form.data
            file = form.file
        # DATAFRAME READ, NOW CLEAR DATA
            data=DataSheet(data_file=file,data_name=name_file)
            data.is_data()
            sheetEnd = RemoveNaN(data)
            sheetEnd.value_cells_isnan()
            sheetEnd.delet_cell()
            sheetEnd.dataframe_exception()       
            download_file = sheetEnd.download_zip()
            return download_file
    else:
        form = postData()
    return render(request,'servermanager/post',{'form':form}) 