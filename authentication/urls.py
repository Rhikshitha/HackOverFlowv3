from django.urls import path,include
from .views import *

urlpatterns = [
    path('register/',register,name="register"),
    path('login/',login,name="login"),
    path('logout/',logout,name="login"),
    path('verify_email/',verify_email,name="verify_email"),
    path('home',home,name="home")

   

]