from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
def home(request):
    return render(request,"index.html")

def passenger(request):
    return render(request,"passangerMap.html")

@csrf_exempt
def set_route(request):
    data = json.loads(request.body.decode('utf-8'))
    print(data)
    return JsonResponse({"data":"Done"})