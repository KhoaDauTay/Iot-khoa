from rest_framework import viewsets
from .serializers import NodeSerializer, GardenSerializer
from dashboard.models import Node, Garden


class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer


class GardenViewSet(viewsets.ModelViewSet):
    queryset = Garden.objects.all()
    serializer_class = GardenSerializer
