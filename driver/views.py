from django.shortcuts import render,HttpResponse, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from route_scheduler.models import *
import jwt
from django.contrib import messages
from geopy.geocoders import Nominatim
import ast

def driver(request):
    return render(request,"driverMap.html")

@csrf_exempt
def createrouteplan(request):
    try:
        token = request.COOKIES.get('jwt')
        if not token:
            print(token)
            return redirect("login")
        data = json.loads(request.body.decode('utf-8'))
        route_array=data["array"]
        date=data['route_date']
        time=data['route_time']
        capacity=data['capacity']
        price=data['price']
        source=route_array[0]
        destination=route_array[-1]
        try:
            user_id=jwt.decode(token,'sanjay@123',algorithms='HS256')['id']
            user=CustomUser.objects.get(auth_user_id=user_id)
            try:
                route_plan = RoutePlan.objects.update_or_create(
                    user_mapped=user,
                    start_location=source,
                    end_location=destination,
                    date=date,
                    time=time,
                    price=price,
                )
                try:
                    ride=Ride.objects.update_or_create(
                        driver=user,
                        max_capacity=capacity,
                        route_plan=route_plan[0]
                    )
                    render_data={
                        'user_mapped':user,
                        'start_location':source,
                        'end_location':destination,
                        'date':date,
                        'time':time,
                        'price':price,
                        'max_capacity':capacity,
                    }
                except Exception as e:
                    print("Ride",e)
            except Exception as e:
                print("Route_Plan",e)
        except Exception as e:
            print("Total:",e)
        messages.success(request, 'Route Plan Set!')
        return render(request,'driverMap.html',render_data)
        return JsonResponse({"data":"Success"})
    except Exception as e:
        return HttpResponse(f"{e}")

def getrouteplan(request):
    try:
        token = request.COOKIES.get('jwt')
        if not token:
            print(token)
            return redirect("login")
        try:
            user_id=jwt.decode(token,'sanjay@123',algorithms='HS256')['id']
            print(user_id)
            print("GOt user id")
            geolocator = Nominatim(user_agent="geoapiExercises")
            try:
                user=CustomUser.objects.get(auth_user_id=user_id)
                route_plans=RoutePlan.objects.filter(user_mapped=user)
                data=[]
                for route_plan in route_plans:
                    ride=Ride.objects.get(route_plan=route_plan)
                    start=ast.literal_eval(route_plan.start_location)
                    dest=ast.literal_eval(route_plan.end_location)
                    start_location = geolocator.reverse(f"{start[1]}, {start[0]}")
                    end_location=geolocator.reverse(f"{dest[1]}, {dest[0]}")
                    print(start_location,end_location)
                    temp={
                        'source_location':start_location,
                        'destination_location':end_location,
                        'max_capacity':ride.max_capacity,
                        'charge per km':route_plan.price,
                        'filled_capacity':ride.filled_capacity,
                    }
                    data.append(temp)
                return JsonResponse({'route_plans':data},safe=False)    
            except Exception as e:
                print("GEtting user",e)
        except Exception as e:
            return JsonResponse(f"Inside Try{e}",safe=False)
    except Exception as e:
        return JsonResponse(f"{e}",safe=False)
    
def getpassengerrequest(request):
    try:
        token = request.COOKIES.get('jwt')
        if not token:
            print(token)
            return redirect("login")
        try:
            user_id=jwt.decode(token,'sanjay@123',algorithms='HS256')['id']
            print(user_id)
            data=[]
            user=CustomUser.objects.get(id=user_id)
            ride_reqs=RideRequest.objects.all()
            for ride_req in ride_reqs:
                ride=ride_req.ride
                if(ride.driver==user):
                    temp={
                        'requester':ride_req.requester,
                        'ride':ride
                    }
                    data.append(temp)
            return JsonResponse({'requests':data}, safe=False)
        except Exception as e:
            print(e)
    except Exception as e:
       print(e)