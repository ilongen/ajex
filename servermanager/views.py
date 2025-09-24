from django.shortcuts import render
from servermanager.services.DataSheet import DataSheet
from servermanager.services.modelsReady.CleanCell.RemoveNaN import RemoveNaN
from django.http import HttpResponse
import pandas
# Create your views here.

def index(request):
    return render(request,template_name='index.html')

def models_ready(request):
    return render(request,template_name="models-ready.html")

def cleanCeLL(request):
    return render(request,template_name="cleancell.html")

def postForm(request):
    # Request received from frontend
    if request.method == 'POST':
        inputfile = request.FILES.get('inputFile')
        data=DataSheet(data_input=inputfile)
        try:
            df = data.is_sheet()
            sheetEnd = RemoveNaN(df=df)
            sheetEnd.value_cells_isnan()
            sheetEnd.delet_cell()
            sheetEnd.dataframe_exception()       
            download_file = sheetEnd.download_zip()
            return download_file
        except Exception as e:
            return HttpResponse(f'Servidor não conseguiu processador os dados devido a: {e}')
    else:
        return HttpResponse('Não foi possível limpar...')