from .models import RegisteredVehicle
from rest_framework import serializers


class RegisteredVehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisteredVehicle
        fields = "__all__"