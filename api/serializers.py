from rest_framework import serializers
from project.models import UserSignIn,UserSignUp

class UserAdd(serializers.ModelSerializer):
    class Meta:
        model = UserSignIn
        fields = ('id', 'email', 'first_name', 'last_name','password','username')
        read_only_fields = ('id',)
class UserAccess(serializers.ModelSerializer):
    class Meta:
        model = UserSignUp
        fields = {'id','username','password'}
        read_only_fields = ('id',)
