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
        source=route_array[0]
        destination=route_array[-1]
        try:
            user_id=jwt.decode(token,'sanjay@123',algorithms='HS256')['id']
            print(user_id)
            user=CustomUser.objects.get(auth_user_id=user_id)
            print(user)
            print("Ellam technology")
            try:
                route_plan = RoutePlan.objects.update_or_create(
                    user_mapped=user,
                    start_location=source,
                    end_location=destination,
                    date=date,
                    time=time,
            )
                print("TEst")
                route_plan.save()
            except Exception as e:
                print(e)
        except Exception as e:
            print("Ex:",e)
        
        return JsonResponse({"data":"Success"})
    except Exception as e:
        return HttpResponse(f"{e}")
