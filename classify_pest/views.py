from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, "classify_pest/index.html")

def about(request):
    return render(request, "classify_pest/about.html")

def mainpage(request):
    return render(request, "classify_pest/main.html")