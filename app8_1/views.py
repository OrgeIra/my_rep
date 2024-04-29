from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def view8_2(request):
    return HttpResponse("This is view8_2 of app8_2")

def view8_1(request):
    return HttpResponse("This is view8_1 of app8_2")
