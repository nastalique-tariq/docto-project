from django.urls import path
from . import views

urlpatterns = [
    path('recommended-doctors/<str:id>', views.doctorrecommendation, name= 'doctor-recommendation'),
]