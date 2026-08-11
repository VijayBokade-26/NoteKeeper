from .models import User
from rest_framework import serializers

class SignUpSerializers(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only = True,required = True)

    class Meta:
        model = User
        fields = ["first_name", "last_name", "email", "phone", "password", "confirm_password", ]

    def validate(self,attrs):
        password = attrs.get("password")
        self.confirm_password  = attrs.pop("confirm_password",None)

        if password != self.confirm_password:
            raise serializers.ValidationError({"confirm_password": "Password do not match"})
        return attrs
    def create(self, validated_data):
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()

        return user

    