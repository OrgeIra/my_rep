from django.shortcuts import render
from django.http import HttpResponse

def view2_1(request):
    return HttpResponse("This is view1 of app2_2")

def view2_2(request):
    return HttpResponse("This is view2 of app2_2)
# Create your views here.
