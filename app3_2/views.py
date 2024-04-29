from django.shortcuts import render
from django.http import HttpResponse

def view3_1(request):
    return HttpResponse("This is view1 of app3_2")

def view3_2(request):
    return HttpResponse("This is view2 of app3_2")
# Create your views here.
