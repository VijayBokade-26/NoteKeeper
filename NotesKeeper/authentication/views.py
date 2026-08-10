from django.shortcuts import render
from users import models as UserModel
from users import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework import exceptions
# Create your views here.
class SignUpView:
    queryset = UserModel.User.objects.all() 
    serializer_class = serializers.SignUpSerializers
    permission_classes = (IsAuthenticated,)
    allowed_methods = ['POST']

    def post(self,request, *args, **kwargs):
        email = request.data.get("email")
        if UserModel.objects.filter(email_i_exact = email).exists():
            raise exceptions.bad_request(data = {'error': "Email is already exists!"})

        
        
            

            



