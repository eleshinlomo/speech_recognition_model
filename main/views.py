from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    test = 'Welcome to Speech Recognition project by MYAFROS'
    return HttpResponse(test)
