from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def view1(request):
    return HttpResponse("This is view1 of app1")

def view2(request):
    return HttpResponse("This is view2 of app1")