from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name="home"),
    path('symptoms-selection/<str:id>/', views.symptoms_selection, name="symptoms_selection"),
    path('predicted-disease/', views.predicted_disease, name="predicted_disease"),
]

