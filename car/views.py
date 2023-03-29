from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.http import HttpResponse
#CRUD

#reading objects
#preview of objects
def car_preview(request):
    car_object = models.Car.objects.all()
    return render(request, 'car_list.html', {'car_object': car_object})


#full-view of id object
def car_full_view(request, id):
    car_full = get_object_or_404(models.Car, id=id)
    return render(request, 'car_full_list.html', {'car_full': car_full})


#creating objects from forms
def create_carobj_view(request):
    method = request.method
    if method == "POST":
        form = forms.CarForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h2 Успешно добавлен в бвзу данных </h2>')
    else:
        form = forms.CarForm()

    return render(request, "create_car.html", {'form': form})


#Удаление из базы
def delete_object_view(request, id):
    car_object = get_object_or_404(models.Car, id=id)
    car_object.delete()
    return HttpResponse('Обьект удален из Базы данных')


def update_object_view(request, id):
    car_object = get_object_or_404(models.Car, id=id)
    if request.method == 'POST':
        form = forms.CarForm(instance=car_object, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Данные успешно обновлены!')
    else:
        form = forms.CarForm(instance=car_object)

    context = {
        'form': form,
        'object': car_object
    }
    return render(request, 'update_car.html', context)


def feedback_view(request, id):
    car_object = get_object_or_404(models.Car, id=id)
    if request.method == 'POST':
        form = forms.FeedbackForm(instance=car_object, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('<h2 Ваш отзыв успешно добавлен в базу данных </h2>')
    else:
        form = forms.FeedbackForm(instance=car_object)

    context = {
        'form': form,
        'object': car_object
    }
    return render(request, 'feedback.html', context)


def catalog_view(request):
    return render(request, 'catalog.html')
    #
    # method = request.method
    # if method == "POST":
    #     form = forms.FeedbackForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return HttpResponse('<h2 Ваш отзыв успешно добавлен в базу данных </h2>')
    # else:
    #     form = forms.FeedbackForm()
    #
    # return render(request, "feedback.html", {'form': form})