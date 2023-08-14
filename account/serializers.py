from rest_framework import serializers 
from .models import RegisteredVehicle

class RegisteredVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisteredVehicle
        fields = "__all__"