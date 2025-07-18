# TIME
from datetime import datetime

# JSON/RESPONSE RESULTS
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view

# DIRS FOR API USERS
from .services.UsersController.SignIn import UserSignIn
from .services.UsersController.SignUp import UserSignUp

# DIRS FOR API MODELS READY
from api.services.ModelsReady import UserData
from api.services.ModelsReady.Yarth import ManipulationData

# START API USERS
# ---------------------------------------------------------------------
# SIGNUP --------------------------------
@api_view(['POST'])
def create_user(request):
    user_name = request.data.get('username')
    user_password = request.data.get('password')
    user_email = request.data.get('email')
    date_joined = datetime.now()

    user_name = user_name.strip() if user_name else None
    user_password = user_password.strip() if user_password else None
    user_email = user_email.strip() if user_email else None

    user = UserSignUp(user_name, user_password, user_email, date_joined)
    
    if user.rules().status_code == status.HTTP_200_OK:
        if user.validation_user_in_db().status_code == status.HTTP_202_ACCEPTED:
            return user.insert_data_in_db()
        else:
            return user.validation_user_in_db()
    else:
        return user.rules()
# END SIGNUP
#--------------------------
# SIGNIN --------------------------------
@api_view(['POST'])
def validated_user(request):
    user_name = request.data.get('username')
    user_password = request.data.get('password')
    user = UserSignIn(username=user_name, password=user_password)
    response = user.exists_user()
    return response
# END SIGNUP
#--------------------------
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

