from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.

class User(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    username=models.CharField(unique=True,max_length=100)
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    contactno = models.CharField(max_length=20)
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default='O',
    )
    token = models.CharField(max_length=32)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
      return self.name
    
    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_sha256'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
