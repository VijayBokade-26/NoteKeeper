from django.shortcuts import render
from users import models as UserModel
from users import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
class SignUpView:
    queryset = UserModel.User.objects.all() 
    serializer_class = serializers.SignUpSerializers
    permission_classes = (IsAuthenticated,)
    allowed_methods = ['POST']

    def post(self,request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        serializer.is_valid(raise_exception = True)
        user = serializer.save()
        return Response(
            {
              "message": "User registerd successfully!",
              "user" : self.serializer_class(user).data      
            }, status = status.HTTP_201_CREATED
        )
        

        
        
        # self.queryset.objects.create)
        

        
        
            

            



