from django.urls import path
from . import views

urlpatterns = [
    path('recommended-doctors/', views.doctorrecommendation, name= 'doctor-recommendation'),
]