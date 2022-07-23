from django.urls import path
from . import views


urlpatterns = [
    path('symptoms-selection/', views.symptoms_selection, name="symptoms_selection"),
    path('predicted-disease/', views.predicted_disease, name="predicted_disease"),
]

