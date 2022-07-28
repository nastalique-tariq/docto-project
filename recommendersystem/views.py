from unicodedata import name
from django.shortcuts import render
from django.http import HttpResponse

def doctorrecommendation(request):
    return render(request, 'doctor-recommendation.html')
