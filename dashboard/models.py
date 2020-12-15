from django.db import models
from django.conf import settings


# Create your models here.

class Node(models.Model):
    name = models.CharField(max_length=255)
    location_name = models.CharField(max_length=50)
    temperature = models.IntegerField(default=0)
    humidity = models.IntegerField(default=0)
    moisture = models.IntegerField(default=0)
    light = models.IntegerField(default=0)
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} in {self.location_name}"


class Garden(models.Model):
    name = models.CharField(max_length=50)
    device = models.ForeignKey(
        Node,
        null=False,
        on_delete=models.CASCADE
    )
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
