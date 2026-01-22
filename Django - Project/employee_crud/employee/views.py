from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'employee/index.html')

def empList(request):
    return render(request, 'employee/emp_list.html')

def empRegistration(request):
    return render(request, 'employee/emp_form.html')