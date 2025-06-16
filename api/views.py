# TIME
import datetime


# JSON/RESPONSE RESULTS
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# DIRS FOR API USERS
from .services.UsersController.SignIn import UserSignIn
from .services.UsersController.SignUp import UserSignUp

# DIRS FOR API MODELS READY
from api.services.ModelsReady import UserData
from api.services.ModelsReady.Yarth import ManipulationData

# START API USERS
# ---------------------------------------------------------------------
@api_view(['POST'])
def create_user(request):
    user_name = request.data.get('user_name')
    user_password = request.data.get('user_password')
    user_email = request.data.get('user_email')
    user_first_name = request.data.get('user_first_name')
    user_last_name = request.data.get('user_last_name')
    data_joined = datetime.datetime.now()

    user_name = user_name.strip() if user_name else None
    user_password = user_password.strip() if user_password else None
    user_email = user_email.strip() if user_email else None
    user_first_name = user_first_name.strip() if user_first_name else ''
    user_last_name = user_last_name.strip() if user_last_name else ''

    user = UserSignUp(user_name, user_password, user_email, user_first_name, user_last_name, data_joined)
    if user.rules().status_code == status.HTTP_200_OK:
        return user.insert_data_in_db()
    else:
        return user.rules()

@api_view(['GET'])
def validated_user(request):
    user_name = request.data.get('user_name')
    user_password = request.data.get('user_password')

    user = UserSignIn(user_name, user_password)

# END API USERS
# ---------------------------------------------------------------------
def model_yarth(request):
    # Request received from frontend
    if request.method == "POST":

        # POST REQUEST SUCESS
        file=request.POST.get('fileSheet') # File request
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

