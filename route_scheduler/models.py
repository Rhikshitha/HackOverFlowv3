from django.db import models
from authentication.models import User
# from django.contrib.gis.db import models as  # gis_models

class CustomUser(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    PREFERENCES=[
        ('shared', 'Shared Ride'),
        ('individual', 'Individual Ride')
    ]
    GENDER_PREFERENCE_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('A', 'Any Gender'),
    ]
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, unique=True)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default='O',
    )
    auth_user_id=models.IntegerField(primary_key=True)
    vehicle_preference = models.CharField(max_length=20, choices=PREFERENCES)
    gender_preference=models.CharField(max_length=1, choices=GENDER_PREFERENCE_CHOICES, blank = True, null=True) 
    route_plan=models.ForeignKey('RoutePlan',on_delete=models.CASCADE,null=True,blank=True)
    
class RoutePlan(models.Model):
    user_mapped = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='route_plans')
    start_location = models.CharField(max_length=200)
    end_location = models.CharField(max_length=200)
    date = models.DateField()
    time = models.TimeField()
    is_recurring = models.BooleanField(default=False,null=True,blank=True)

class Ride(models.Model):
    driver = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='rides_offered')
    passengers = models.ManyToManyField(CustomUser, related_name='rides_taken', blank=True)
    max_capacity=models.IntegerField()
    filled_capacity = models.IntegerField(default=0)
    route_plan=models.OneToOneField(RoutePlan, on_delete=models.CASCADE)
   # start_location =  # gis_models.PointField(geography=True, null=True, blank=True)
   # end_location = gis_models.PointField(geography=True, null=True, blank=True)
    date = models.DateTimeField()
    
class RideRequest(models.Model):
    requester = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='requests_made')
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE, related_name='ride_requests')
    message = models.TextField()
    is_accepted = models.BooleanField(default=False)

class CostShare(models.Model):
    ride = models.OneToOneField(Ride, on_delete=models.CASCADE, related_name='cost_share')
    total_cost = models.FloatField()
    driver_share = models.FloatField()
    passenger_share = models.FloatField()

class Rating(models.Model):
    rated_user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='ratings_received')
    rated_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='ratings_given')
    stars = models.IntegerField()
    reviews = models.TextField()
