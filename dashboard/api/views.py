from random import randint

from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .serializers import NodeSerializer, GardenSerializer
from dashboard.models import Node, Garden


class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer


class GardenViewSet(viewsets.ModelViewSet):
    queryset = Garden.objects.all()
    serializer_class = GardenSerializer
