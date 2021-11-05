from django.db import models
from django.utils import timezone

# Create your models here.

class Adviser(models.Model):
    adviser_id=models.AutoField(primary_key=True)
    adviser_name=models.CharField(max_length=100,unique=True)
    adviser_photo=models.FileField(upload_to='booking_user/adviser_pics/',null=True,blank=True)
    adviser_photo_url=models.URLField()

    def __str__(self):
        return self.adviser_name

class User(models.Model):
    id=models.AutoField(primary_key=True)
    user_name=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    password=models.CharField(max_length=50)

    def __str__(self):
        return self.user_name

class Booking(models.Model):
    booking_id=models.AutoField(primary_key=True)
    adviser=models.ForeignKey(Adviser,on_delete=models.CASCADE)
    booking_time=models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.adviser.adviser_name