from django import urls
from django.contrib import admin
from django.urls import path, include



urlpatterns = [
    path('admin/', admin.site.urls),
    path('disease-predictor/', include('diseaseprediction.urls')),
    path('recommender/', include('recommendersystem.urls'))
]
