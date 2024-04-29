from django.shortcuts import render
from django.http import HttpResponse

def view4_1(request):
    return HttpResponse("This is view1 of app4_1")

def view4_2(request):
    return HttpResponse("This is view2 of app4_2")
# Create your views here.
