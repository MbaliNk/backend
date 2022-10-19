from importlib.resources import path
from django.urls import path
from .views import buyProducts


urlpatterns = [
    path("",buyProducts),
    
    ]