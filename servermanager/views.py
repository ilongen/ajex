from django.shortcuts import render

# Create your views here.

def index(request):
    template_name = 'index.html'
    return render(request,template_name)

def models_ready(request):
    template_name = "models-ready.html"
    return render(request,template_name)
'''
def model_RemoveNaN(request):
    # Request received from frontend
    if request.method == "POST":

        # Caso o POST for sucesso, ele irá enviar pro servidor a informação.
        file=request.POST.get('file') # File request
        name_file = file.name
        file = file.read()
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
        JsonResponse({"error":"Method not allowed"})
    return None

'''