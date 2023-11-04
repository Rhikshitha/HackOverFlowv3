from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def home(request):
    return render(request,"index.html")

def passenger(request):
    return render(request,"passangerMap.html")

@csrf_exempt
def set_route(request):
    source=request.POST.get("source")
    destination=request.POST.get("destination")
    return JsonResponse({"data":"Done"})