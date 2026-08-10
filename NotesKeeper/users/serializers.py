from .models import User
from rest_framework import serializers

class SignUpSerializers(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only = True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "phone", "password", "confirm_password", ]

    def validate(self,attributes):
        pass


    