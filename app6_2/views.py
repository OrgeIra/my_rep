from django.shortcuts import render
from django.http import HttpResponse

def view6_1(request):
    return HttpResponse("This is view6_1 of app6_1")

def view6_2(request):
    return HttpResponse("This is view6_2 of app6_1")

# Create your views here.
