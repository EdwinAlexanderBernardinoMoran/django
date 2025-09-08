from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:day>/', views.days_weeks_numbers, name='day_number'),
    path('<str:day>/', views.days_weeks, name='day')
]
