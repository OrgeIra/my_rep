from django.shortcuts import render
from django.http import Httpresponse
# Create your views here.


def view9_1(request):
    return HttpResponse("This is view9_1 of app9_1")


def view9_2(request):
    return HttpResponse("This is view9_2 of app9_1")