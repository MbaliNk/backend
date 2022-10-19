from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def buyProducts(request):
    return HttpResponse("Welcome to Gossip girl product page ")

