from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Home Page")

def diseaseprediction(request):
    return HttpResponse("Select your symptoms!")