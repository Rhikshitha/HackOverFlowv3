from django.urls import path,include
from .views import *

urlpatterns = [
    path('',driver,name="driver"),
    path('createrouteplan/',createrouteplan,name="createrouteplan"),
    path('getrouteplan/',getrouteplan,name="getrouteplan"),
    path('getpassengerrequest/',getpassengerrequest,name="getpassengerrequest"),
]