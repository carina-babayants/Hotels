from django.urls import path
from . import views

urlpatterns = [
    path('', views.hotels_list_list, name="hotels_list"),
    path('single/<int:pk>', views.hotel_list_single, name="hotel_list_single"),
]