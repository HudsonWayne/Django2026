from django.shortcuts import render
from .models import User

def home(request):
    users = User.objects.all()  # fetch all users from DB
    return render(request, 'core/home.html', {"users": users})


def create_user(request):
    if request.method == "POST":
        form = UserForm(request.Post)