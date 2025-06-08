from django.http import JsonResponse
from django.shortcuts import render
from api.services.ManipulationData import ManipulationData
from api.services.UserData import UserData

# Create your views here.

def index(request):
    return render(request,"index.html")

"""
    API: user_data
    modified: 04/05/2025 | 01:31 PM
    describe: This api works on receiving data and preparing for other api/backend services.

"""
def user_data(request):
    # Request received from frontend
    if request.method == "POST":

        # POST REQUEST SUCESS
        file=request.FILES.get('fileSheet') # File request
        name_file = file.name
        file = file.read()
        df_transform = UserData(user_data_name=name_file,user_data_file=file)
        df_optimized = df_transform.get_data()
        # DATAFRAME READ, NOW CLEAR DATA
        sheet_manipulation=ManipulationData(df=df_optimized)
        sheet_manipulation.value_cells_isnan()
        sheet_manipulation.delet_cell()
        sheet_manipulation.dataframe_exception()
        download_file = ManipulationData.download_zip(self=sheet_manipulation)
        return download_file
    else:
        JsonResponse({"error":"Method not allowed"})
    return None
