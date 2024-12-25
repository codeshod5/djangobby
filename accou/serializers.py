from rest_framework import serializers
from .models import UserSignup

class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSignup
        fields = ['id','email','area','timing']

class UserSignupDeatails(serializers.ModelSerializer):
    class Meta:
        model = UserSignup
        fields = ['email','area','timing']

