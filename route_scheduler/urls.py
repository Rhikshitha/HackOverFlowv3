from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('passenger/',passenger,name="passenger"),
    path('find_voyager/',find_voyager,name="find_voyager"),
    path('profile/',profile,name="profile"),

]