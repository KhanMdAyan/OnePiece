from django.http.response import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')
def base(request):
    return render(request, 'home.html')