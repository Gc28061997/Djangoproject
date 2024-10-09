# employee/views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee
from django.views.decorators.csrf import csrf_exempt

import json

# Function to render home page
def home(request):
    return render(request, 'employee/home.html')

def employee_list(request):
    employees = Employee.objects.all()
    print("Employees found:", employees)  # This will log to the console
    return render(request, 'employee/list.html', {'employees': employees})

# Fetch all employees and return as JSON
def load_employees(request):
    employees = Employee.objects.all().values()  # Fetch all employee records
    return JsonResponse(list(employees), safe=False)  # Return as JSON

# Function to list all employees
def listEmployees(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        # Handle AJAX request
        employees = Employee.objects.all()  # Retrieve all employees
        data = {
            'employees': list(employees.values()),  # Serialize the employee data
        }
        return JsonResponse(data)  # Return the data as JSON
    else:
        # Handle regular request
        return render(request, 'employee/list.html')

# Function to create a new employee
def createEmployee(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            employee = Employee(
                name=data['name'],
                email=data['email'],
                age=data['age'],
                gender=data['gender'],
                phone_no=data['phoneNo'],
                address_details=data['addressDetails'],
                work_experience=data.get('workExperience', []),
                qualifications=data.get('qualifications', []),
                projects=data.get('projects', [])
            )
            employee.save()
            return JsonResponse({'message': 'Employee created successfully!'}, status=201)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

# Function to update an employee
@csrf_exempt  # Only if you're not using CSRF tokens (which is not recommended for production)
def updateEmployee(request, id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            # Assuming you have an Employee model
            employee = Employee.objects.get(id=id)
            
            # Update employee fields from the received data
            employee.name = data.get('name', employee.name)
            employee.email = data.get('email', employee.email)
            employee.age = data.get('age', employee.age)
            employee.gender = data.get('gender', employee.gender)
            employee.save()

            return JsonResponse({'message': 'Employee updated successfully'})
        except Employee.DoesNotExist:
            return JsonResponse({'error': 'Employee not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
# Delete Employee
@csrf_exempt  # Only if you want to allow non-CSRF requests (not recommended)
def deleteEmployee(request, id):
    if request.method == 'DELETE':
        try:
            employee = Employee.objects.get(id=id)
            employee.delete()
            return JsonResponse({'message': 'Employee deleted successfully.'})
        except Employee.DoesNotExist:
            return JsonResponse({'error': 'Employee not found.'}, status=404)
    return JsonResponse({'error': 'Invalid request method.'}, status=405)