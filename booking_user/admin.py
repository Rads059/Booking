from django.contrib import admin
from .models import Adviser,User,Booking

# Register your models here.

admin.site.register(Adviser)
admin.site.register(Booking)
admin.site.register(User)