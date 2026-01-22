from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('employee-list', views.empList, name='emp-list'),
    path('registration-form', views.empRegistration, name='emp-form'),
]