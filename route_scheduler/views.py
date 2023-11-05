from django.shortcuts import render,HttpResponse,redirect
# from django.contrib.gis.geos import LineString, Point
# from django.contrib.gis.db.models.functions import Distance
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .utils import *
from .models import *
import jwt
from django.views.decorators.http import require_POST
from .serializer import CustomUserSerializer


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
    try:
        token = request.COOKIES.get('jwt')
        if not token:
            return redirect("login")

        data = json.loads(request.body.decode('utf-8'))
        user_id=jwt.decode(token,'sanjay@123',algorithms='HS256')['id']
        try:
            user=CustomUser.objects.get(auth_user_id=user_id)
        except:
            return JsonResponse({"message":"user not found"})

        print(data)
        source=data["source"]
        destination=data["destination"]
        route_time=data["route_time"]
        route_date=data["route_date"]
        

        
        return JsonResponse({"message":"success"})
    except Exception as e:
         return JsonResponse({"message":f"failed:{e}"})




def profile(request):
    try:
        token = request.COOKIES.get('jwt')
        if not token:
            return redirect("login")
        
        user_id=jwt.decode(token,'sanjay@123',algorithms='HS256')['id']
        if request.method=="POST":
            gender_preference=request.POST.get("genderPreference")
            vehical_preference=request.POST.get("vehiclePreference")
            update_values = {
                'vehicle_preference': vehical_preference,  # Update vehicle preference
                'gender_preference': gender_preference,  # Update gender preference to 'Any Gender'
            }
            user=User.objects.get(id=user_id)
            try:
                cus_user=CustomUser.objects.filter(auth_user_id=user_id)
                if len(cus_user)==0:
                    pro=CustomUser.objects.create(
                        name=user.name,
                        email=user.email,
                        gender=user.gender,
                        auth_user_id=user_id,
                        vehicle_preference=vehical_preference,
                        gender_preference=gender_preference
                    )
                else:
                    cus_user.update(vehicle_preference=vehical_preference,gender_preference=gender_preference)
                    return redirect("/")
            except Exception as e:
                return JsonResponse({"message": f"Failed :{str(e)}"})
                
        else:
            cus_user=CustomUser.objects.filter(auth_user_id=user_id)
            if len(cus_user)==0:
                return redirect("/profile/")
            else:
                cus_user=cus_user[0]
                serializer = CustomUserSerializer(cus_user)
                print(serializer.data)
                return render(request,'createProfile.html',serializer.data)

    except Exception as e:
        return JsonResponse({"message": f"Failed :{str(e)}"})

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
  
