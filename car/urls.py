from django.urls import path
from . import views

urlpatterns = [
    path('car_list/', views.car_preview, name='car_list'),
    path('car_list/<int:id>/', views.car_full_view, name='car_full'),
    path('car_list/<int:id>/delete/', views.delete_object_view, name='delete'),
    path('car_list/<int:id>/update/', views.update_object_view, name='update'),
    path('create_car/', views.create_carobj_view, name='create'),
    path('car_list/<int:id>/feedback/', views.feedback_view, name='feedback'),
    path('catalog_list/', views.catalog_view, name='catalog'),

]