from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    user = [
        {"name": "Wayne", "is_active": True},
    ]