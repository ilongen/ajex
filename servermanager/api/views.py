# TIME
from datetime import datetime

# JSON/RESPONSE RESULTS
from django.http import JsonResponse

# DIRS FOR API MODELS READY
from api.services.ModelsReady import User
from api.services.ModelsReady.CleanCell import RemoveNaN

# START API
# ---------------------------------------------------------------------
def model_RemoveNaN(request):
    # Request received from frontend
    if request.method == "POST":

        # Caso o POST for sucesso, ele irá enviar pro servidor a informação.
        file=request.POST.get('fileSheet') # File request
        name_file = file.name
        file = file.read()
        df_transform = User
        df_optimized = df_transform.get_data()
        # DATAFRAME READ, NOW CLEAR DATA
        sheet_manipulation=RemoveNaN(df_optimized)
        sheet_manipulation.value_cells_isnan()
        sheet_manipulation.delet_cell()
        sheet_manipulation.dataframe_exception()
        download_file = RemoveNaN.download_zip(self=sheet_manipulation)
        return download_file
    else:
        JsonResponse({"error":"Method not allowed"})
    return None

