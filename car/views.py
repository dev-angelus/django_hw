from django.shortcuts import render, get_object_or_404
from . import models


#preview of objects
def car_preview(request):
    car_object = models.Car.objects.all()
    return render(request, 'car_list.html', {'car_object': car_object})


#full-view of id object
def car_full_view(request, id):
    car_full = get_object_or_404(models.Car, id=id)
    return render(request, 'car_full_list.html', {'car_full': car_full})

