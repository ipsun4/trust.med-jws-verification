import json

from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.

def index(request):
    with open("../scripts/did.json") as did_file:
        parsedJson = json.load(did_file)

    return JsonResponse(parsedJson)
