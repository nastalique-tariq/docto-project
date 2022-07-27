from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')


def symptoms_selection(request):
    return render(request, "symptoms-selection.html")

def predicted_disease(request):
    return render(request, "disease-prediction.html")

