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
        try:
            inputfile = request.FILES.get('inputFile')
            data=DataSheet(data_input=inputfile)
            df = data.is_sheet()
            sheetEnd = RemoveNaN(df=df)
            sheetEnd.value_cells_isnan()
            sheetEnd.delet_cell()
            sheetEnd.dataframe_exception()       
            download_file = sheetEnd.download_zip()
            return download_file
        except Exception as e:
            raise e
    else:
        return HttpResponse('Erro de servidor interno: O arquivo não foi limpo, função não executou de maneira esperada.')