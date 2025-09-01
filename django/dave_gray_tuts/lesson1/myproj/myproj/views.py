# from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Welcome to the Home Page")
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("Welcome to the About Page")
    return render(request, 'about.html')