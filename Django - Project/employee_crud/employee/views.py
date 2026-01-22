from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee
from .forms import EmployeeForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'employee/index.html')

def empList(request):
    employees = Employee.objects.all()
    return render(request, 'employee/emp_list.html', {'employees': employees})

def empRegistration(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee Registered Successfully!')
            return redirect('emp-list')
    else:
        form = EmployeeForm()
    return render(request, 'employee/emp_form.html', {'form': form})

def empUpdate(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee Details updated successfully!')
            return redirect('emp-list')
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'employee/emp_form.html', {'form': form})

def empDelete(request, pk):
    employee = get_object_or_404(Employee, pk=pk)
    if request.method == 'POST':
        employee.delete()
        messages.success(request, 'Employee Details deleted successfully!')
        return redirect('emp-list')
    return render(request, 'employee/emp_delete.html', {'employee': employee})