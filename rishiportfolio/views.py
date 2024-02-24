# This file is created by me

from django.shortcuts import render
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def certificate(request):
    return render(request, 'certificate.html')