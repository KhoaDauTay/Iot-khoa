from random import randint

from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .serializers import NodeSerializer, GardenSerializer
from dashboard.models import Node, Garden


class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer

    def retrieve(self, request, pk=id):
        node = get_object_or_404(self.queryset, pk=pk)
        node.temperature = randint(80, 100)
        node.humidity = randint(20, 30)
        node.moisture = randint(60, 80)
        node.light = randint(80, 100)
        node.save()
        serializer = self.serializer_class(node)
        return Response(serializer.data)


class GardenViewSet(viewsets.ModelViewSet):
    queryset = Garden.objects.all()
    serializer_class = GardenSerializer
