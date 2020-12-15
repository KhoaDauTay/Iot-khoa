from django.urls import path, include

from . import views

urlpatterns = [
    path('device/<int:device_id>/', views.get_devices, name='devices'),
    path('dashboard/', views.get_dashboard, name='dash-board'),
]
