import datetime

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .services.UsersController.SignIn import UserSignIn
@api_view(['POST'])
def post_user_data(request):
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

    user = UserSignIn(user_name, user_password, user_email, user_first_name, user_last_name, data_joined)
    if user.rules().status_code == status.HTTP_200_OK:
        return user.insert_data_in_db()
    else:
        return user.rules()
