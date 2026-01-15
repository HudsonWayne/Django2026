from django.urls import path
from .views import home, create_user

urlpatterns = [
    path('', home, name='home'),
    path('create/', create_user, name='create_user'),
]
