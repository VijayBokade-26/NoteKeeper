from authentication.models import OTP
from datetime import  datetime
import pytz
from django.conf import settings
from .models import User
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import exceptions 
from rest_framework import status
from django.contrib.auth.hashers import check_password, make_password

class SignUpSerializers(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only = True,required = True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "phone", "password", "confirm_password", ]

    def validate(self,attrs): #attrs contains the payload which user provided into api 
        password = attrs.get("password")
        self.confirm_password  = attrs.pop("confirm_password",None)

        if password != self.confirm_password:
            raise serializers.ValidationError({"confirm_password": "Password do not match"})
        return attrs
    
    def create(self, validated_data): #serializer.save() will call this method and create a new entry. 
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        return user


class LoginSerializer(TokenObtainPairSerializer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["otp"] = serializers.CharField(max_length = 10)

    def validate(self,attrs):
        email = attrs.get("email")
        password = attrs.get("password")
        otp = attrs.get("otp")

        if not otp:
            raise exceptions.AuthenticationFailed(
                {
                    "status": f"error: {status.HTTP_401_UNAUTHORIZED}",
                    "message": "OTP is Required!",
                    "result": {}
                }
            )
        if not email:
            raise exceptions.AuthenticationFailed(
                {
                    "status": f"error: {status.HTTP_401_UNAUTHORIZED}",
                    "message": "email is Required!",
                    "result": {}
                }
            )
        if not password:
            raise exceptions.AuthenticationFailed(
                {
                    "status": f"error: {status.HTTP_401_UNAUTHORIZED}",
                    "message": "password is Required!",
                    "result": {}
                }
            )

        self.user = User.objects.filter(email__iexact = email).first()
        if not self.user:
            raise exceptions.AuthenticationFailed(   
                {
                    "status": f"error: {status.HTTP_401_UNAUTHORIZED}",
                    "message": "Invalid Credentials!",
                    "result": {}
                }
            )
        if not check_password(password, self.user.password):
            raise exceptions.AuthenticationFailed(
                            {
                                "status": f"error: {status.HTTP_401_UNAUTHORIZED}",
                                "message": "Password is wrong!/Invalid Credentials!",
                                "result": {}
                            }
                        )

        current_time = datetime.now(pytz.timezone(settings.TIME_ZONE))

        otp = OTP.objects.filter(user = self.user, otp_type=  1, otp = otp, expired_at__gt = current_time ).first() 
        if not otp:
            raise exceptions.AuthenticationFailed(
                {
                    "status":f"error: {status.HTTP_401_UNAUTHORIZED}",
                    "message": "OTP is invalid! or Expired please try again",
                    "result":{}
                }
            )                                                                                        
        token = TokenObtainPairSerializer.get_token(self.user)
        if not self.user.is_active:
            raise exceptions.AuthenticationFailed(
                {
                    "status": "error",
                    "message": "User is not active! Please contact Admin",
                    'result': {}
                }
            )
        data = {}
        data['refresh'] = str(token)
        data["access"] = str(token.access_token)
        current_time = datetime.now(pytz.timezone(settings.TIME_ZONE))
        self.user.last_login = current_time
        self.user.save(update_fields=["last_login"])
        otp.delete()
        return data

    

