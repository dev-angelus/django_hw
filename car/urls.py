from django.urls import path
from . import views

urlpatterns = [
    path('car_list/', views.car_preview, name='car_list'),
    path('car_list/<int:id>/', views.car_full_view, name='car_full'),

]