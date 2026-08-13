from django.shortcuts import render
from users import models as UserModel
from users import serializers
from rest_framework.permissions import IsAuthenticated
from rest_framework import exceptions
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
# Create your views here.
class SignUpView(APIView):
    queryset = UserModel.User.objects.all() 
    serializer_class = serializers.SignUpSerializers
    permission_classes = (IsAuthenticated,)
    allowed_methods = ["GET", "POST"]

    def post(self,request, *args, **kwargs):
        try:
            serializer = self.serializer_class(data = request.data)
            serializer.is_valid(raise_exception = True)
            user = serializer.save()
            return Response(
                {
                "message": "User registerd successfully!",
                "user" : self.serializer_class(user).data      
                }, status = status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response({
                    "error": str(e),
                },
                status=status.HTTP_400_BAD_REQUEST,            
            )        

class LoginView(APIView):
    queryset = UserModel.User.objects.all()
    serializer_class = serializers.LoginSerializer
    permission_class = (IsAuthenticated,)
    Allowed_methods = ["GET", "POST"]   

    def post(self, request, *args, **kwargs):
        pass
        # try: 
        #     serializer = self.serializer_class
        #     serializer.is_valid()
            
        

           
        
            

            



