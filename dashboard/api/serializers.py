from dashboard.models import *
from rest_framework import serializers


class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = [
            "temperature",
            "humidity",
            "moisture",
            "light",
        ]


class GardenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garden
        fields = "__all__"
