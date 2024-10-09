# employee/urls.py
from django.urls import path
from .views import home, listEmployees, createEmployee, updateEmployee, deleteEmployee, load_employees

urlpatterns = [
    path('', home, name='home'),
    path('list/', listEmployees, name='listEmployees'),
    path('create/', createEmployee, name='createEmployee'),
    path('update/<int:id>/', updateEmployee, name='update_employee'),
    path('delete/<int:id>/',deleteEmployee, name='delete_employee'),
    path('load-employees/', load_employees, name='load_employees'),
]
