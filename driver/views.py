from django.shortcuts import render,HttpResponse, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from route_scheduler.models import *
import jwt
 
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
                )
                try:
                    ride=Ride.objects.update_or_create(
                        driver=user,
                        max_capacity=capacity,
                        route_plan=route_plan[0]
                    )
                    ride.save()
                except Exception as e:
                    print("Ride",e)
            except Exception as e:
                print("Route_Plan",e)
        except Exception as e:
            print("Total:",e)
        return JsonResponse({"data":"Success"})
    except Exception as e:
        return HttpResponse(f"{e}")
