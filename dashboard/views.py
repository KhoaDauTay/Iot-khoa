from django.shortcuts import render, redirect

from dashboard.models import Node


# Create your views here.


def index(request):
    return render(request, 'home.html')


def get_dashboard(request):
    if request.user.is_authenticated:
        user = request.user
        devices = Node.objects.all()
        context = {
            "devices": devices,
            "user": user,
            "title": f"Profile {user.username}"
        }
        return render(request, 'profile.html', context)
    else:
        return redirect('index')


def get_devices(request, device_id):
    if request.user.is_authenticated:
        user = request.user
        devices = Node.objects.all()
        current_device = Node.objects.get(id=device_id)
        context = {
            "devices": devices,
            "current_device": current_device,
            "user": user,
            "title": f"Device - {current_device.name}"
        }
        return render(request, 'dashboard.html', context)
    else:
        return redirect('index')