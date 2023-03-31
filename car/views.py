from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.http import HttpResponse
#CRUD
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView


class CarListView(ListView):
    template_name = 'car_list.html'
    queryset = models.Car.objects.all()

    def get_queryset(self):
        return models.Car.objects.all()

#reading objects
#preview of objects
# def car_preview(request):
#     car_object = models.Car.objects.all()
#     return render(request, 'car_list.html', {'car_object': car_object})


#full-view of id object
class CarDetailView(DetailView):
    template_name = 'car_full_list.html'

    def get_object(self, **kwargs):
        car_id = self.kwargs.get('id')
        return get_object_or_404(models.Car, id=car_id)

# def car_full_view(request, id):
#     car_full = get_object_or_404(models.Car, id=id)
#     return render(request, 'car_full_list.html', {'car_full': car_full})
#

#creating objects from forms


class CreateCarView(CreateView):
    template_name = 'create_car.html'
    form_class = forms.CarForm
    queryset = models.Car.objects.all()
    success_url = '/car_list/'

    def form_valid(self, form):
        print(form.clean)
        return super(CreateCarView, self).form_valid(form=form)


# def create_carobj_view(request):
#     method = request.method
#     if method == "POST":
#         form = forms.CarForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h2 Успешно добавлен в бвзу данных </h2>')
#     else:
#         form = forms.CarForm()
#
#     return render(request, "create_car.html", {'form': form})


#Удаление из базы

class CarDeleteView(DeleteView):
    template_name = 'confirm_delete.html'
    success_url = '/car_list/'

    def get_object(self, **kwargs):
        car_id = self.kwargs.get('id')
        return get_object_or_404(models.Car, id=car_id)


# def delete_object_view(request, id):
#     car_object = get_object_or_404(models.Car, id=id)
#     car_object.delete()
#     return HttpResponse('Обьект удален из Базы данных')
#
class CarUpdateView(UpdateView):
    template_name = 'update_car.html'
    form_class = forms.CarForm
    success_url = '/car_list/'

    def get_object(self, **kwargs):
        car_id = self.kwargs.get('id')
        return get_object_or_404(models.Car, id=car_id)

    def form_valid(self, form):
        print(form.clean)
        return super(CarUpdateView, self).form_valid(form=form)


# def update_object_view(request, id):
#     car_object = get_object_or_404(models.Car, id=id)
#     if request.method == 'POST':
#         form = forms.CarForm(instance=car_object, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('Данные успешно обновлены!')
#     else:
#         form = forms.CarForm(instance=car_object)
#
#     context = {
#         'form': form,
#         'object': car_object
#     }
#     return render(request, 'update_car.html', context)

class CarFeedback(CreateView):
    template_name = 'feedback.html'
    form_class = forms.FeedbackForm
    queryset = models.CarReview.objects.all()
    success_url = '/car_list/'

    def get_object(self, **kwargs):
        review_id = self.kwargs.get('id')
        return get_object_or_404(models.CarReview, id=review_id)

    def form_valid(self, form):
        print(form.clean)
        return super(CarFeedback, self).form_valid(form=form)

# def feedback_view(request, id):
#     car_object = get_object_or_404(models.Car, id=id)
#     if request.method == 'POST':
#         form = forms.FeedbackForm(instance=car_object, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h2 Ваш отзыв успешно добавлен в базу данных </h2>')
#     else:
#         form = forms.FeedbackForm(instance=car_object)
#
#     context = {
#         'form': form,
#         'object': car_object
#     }
#     return render(request, 'feedback.html', context)


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