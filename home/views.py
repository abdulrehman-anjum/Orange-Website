from django.shortcuts import render, get_object_or_404, redirect
from home.models import Employee
from django.forms import ModelForm

# Create your views here.

def index(request):
    return render(request, 'index.html')


def show_employees(request):
    employees = Employee.objects.all()
    return render(request, 'employees.html', {'employees': employees})


def delete_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    employee.delete()
    return redirect('show_employees')


class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'email', 'phone_number', 'department']


def update_employee(request, id):
    employee = get_object_or_404(Employee, id=id)
    if request.method == "POST":
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('show_employees')
        else:
            print(form.errors)
    else:
        form = EmployeeForm(instance=employee)
    return render(request, 'update.html', {'form': form, 'employee': employee})


def register(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            employee = form.save()
            return render(request, 'success.html', {'employee': employee})
    else:
        form = EmployeeForm()
    return render(request, 'register.html', {'form': form})