from django.contrib import admin
from . import models
from car.models import Car

# admin.site.register(models.Car)
admin.site.register(models.Car)
admin.site.register(models.CarReview)
# Register your models here.
