from django.http import HttpResponse
from models.recommender import recommender
import json

def doctorrecommendation(request, id):
    res = recommender.recommend_doctor(id)
    return HttpResponse(json.dumps(res), content_type="application/json")

