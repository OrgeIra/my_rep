from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def view7_2(request):
    return HttpResponse("This is view7_2 of app7_2")

def view7_1(request):
    return HttpResponse("This is view7_1 of app7_2")
    