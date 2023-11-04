from django.shortcuts import render,HttpResponse,redirect
# from django.contrib.gis.geos import LineString, Point
# from django.contrib.gis.db.models.functions import Distance
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import *
from django.views.decorators.http import require_POST


# Create your views here.

def home(request):
    try:
        token = request.COOKIES.get('jwt')
        if not token:
            print(token)
            return redirect("login")

            
        return render(request,"index.html")
    except Exception as e:
        return HttpResponse(f"{e}")

def passenger(request):
    try:
        token = request.COOKIES.get('jwt')
        if not token:
            print(token)
            return redirect("login")
       

        return render(request,"passangerMap.html")
    except Exception as e:
        return HttpResponse(f"{e}")


@csrf_exempt
def find_voyager(request):
    data = json.loads(request.body.decode('utf-8'))
    route=data["route"]
    route_array=data["array"]
    print(route_array)
    return JsonResponse({"data":"Done"})

# @require_POST
def profile(request):
     try:
        token = request.COOKIES.get('jwt')
        if not token:
            print(token)
            return redirect("login")
        try:
            print(request.method)
            if (request.method=='POST'):
                vehiclePreference= request.POST.get("vehiclePreference")
                genderPreference= request.POST.get("genderPreference")
                print(vehiclePreference)
                print(genderPreference)
                return redirect("/")
            else:
                return render(request,"createProfile.html")
        except Exception as e:
            return JsonResponse(f"{e}",safe=False)
        
 
        

     except Exception as e:
        return JsonResponse(f"{e}")
    


def driver(request):
    try:
        token = request.COOKIES.get('jwt')
        if not token:
            print(token)
            return redirect("login")
        
        if request.method=="POST":
            data = json.loads(request.body.decode('utf-8'))
            
            route_array = data['array']
            


            given_coordinates = [80.0055, 13.0095]  # Example given coordinates

            max_distance_in_meters = 500  # Maximum allowed distance in meters

                            # Check if the given coordinates are nearby any coordinates in the array
            is_nearby = are_coordinates_nearby(given_coordinates, route_array, max_distance_in_meters)

            if is_nearby:
                print("Given coordinates are nearby a point in the array.")
            else:
                print("Given coordinates are not nearby any point in the array.")

                    

            return JsonResponse({"data":"Done"})

        else: 
            return render(request,"driverMap.html")
    except Exception as e:
        return HttpResponse(f"{e}")
  
