import json
from django.shortcuts import render
from django.http import HttpResponse
from models.disease_prediction import disease_prediction

def home(request):
    return render(request, 'home.html')


def symptoms_selection(request, id):
    id_ = id.split('-')
    id_.extend([ -1 for _ in range(17 - len(id_))])
    res = disease_prediction.predict(id_)
    return HttpResponse(json.dumps({"result": res[0]}), content_type="application/json")


def predicted_disease(request, id):
    id_ = id.split('-')
    id_.extend([ -1 for _ in range(17 - len(id_))])
    res = disease_prediction.predict(id_)
    return HttpResponse(json.dumps(res), content_type="application/json")
