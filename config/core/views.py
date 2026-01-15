from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm

def home(request):
    users = User.objects.all()
    return render(request, 'core/home.html', {"users": users})


def create_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserForm()

    return render(request, 'core/create_user.html', {"form": form})
