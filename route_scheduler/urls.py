from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('passenger/',passenger,name="passenger"),
    path('set_route/',set_route,name="set_route"),

]