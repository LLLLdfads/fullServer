from django.shortcuts import render
from django.http import JsonResponse
import json
dressing=False
current_play={}

def f1(request):
    return JsonResponse(
        {
            'name':'xiaoming',
            'age':19
        }
    )
def getInfo(request):
    with open('./app1/data/info.json','r',encoding="utf-8") as f:
        data=json.load(f)
        return JsonResponse(data)

