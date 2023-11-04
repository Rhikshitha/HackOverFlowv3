from django.urls import path,include
from .views import *

urlpatterns = [
    path('',home,name="home"),
    path('passenger/',passenger,name="passenger"),
    path('find_voyager/',find_voyager,name="set_route"),
    path('profile/',profile,name="profile"),

]