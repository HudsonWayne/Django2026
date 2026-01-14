from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    user = [
        {"name": "Wayne", "is_active": True},
        {"name": "Bob", "is_active": False},
        {"name": "Charlie", "is_active": True},
        
    ]