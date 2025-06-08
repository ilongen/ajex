import email

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .services.UsersController.SignIn import UserSignIn
@api_view(['POST'])
def post_user_data(request):
    user_name = request.data.get('user_name')
    user_password = request.data.get('user_password')
    user_email = request.data.get('user_email')

    user_name = user_name.strip() if user_name else None
    user_password = user_password.strip() if user_password else None
    user_email = user_email.strip() if user_email else None

    user = UserSignIn(user_name, user_password, user_email)
    if user.rules().status_code == status.HTTP_200_OK:
        user.insert_data_in_db()
        return Response({'success': 'User data inserted successfully'}, status=200)
    else:
        return Response(user.rules(), status=status.HTTP_400_BAD_REQUEST)