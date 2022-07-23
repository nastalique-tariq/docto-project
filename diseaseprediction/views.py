from django.shortcuts import render
from django.http import HttpResponse

def symptoms_selection(request):
    return HttpResponse("Select your symptoms from Multiselector & click predict!")

def predicted_disease(request):
    return HttpResponse("You are suffering from Gastroesophageal Disease!")

