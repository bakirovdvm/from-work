from django.contrib import admin
from django.urls import path, include
from . import views

#app_name = 'car'
urlpatterns = [
    path('', views.home, name='home'),
    path('car_add', views.car, name='car'),
    path('<int:car_id>/', views.car_detail, name='car_detail'),
    path('car_table', views.car_table, name='car_table'),
    path('css_animation', views.css_animation, name='css_animation'),
    path('css_animation_ex', views.css_animation_ex, name='css_animation_ex')
]
