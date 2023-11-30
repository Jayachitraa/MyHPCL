# from django.shortcuts import render, redirect,get_object_or_404
# from django.contrib.auth import authenticate, login
# from django.contrib import messages
# from .forms import ContractemphpclForm
# from .models import Contractemphpcl

# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('employee_detail') 
#         else:
#            return render(request, 'login.html', {'error': 'Invalid username or password'})

#     return render(request, 'login.html')


# def create_employee(request):
#     if request.method == 'POST':
#         form = ContractemphpclForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, 'Employee details submitted successfully.')  
#             return redirect('ContractEmployee:employee_detail', pk=form.cleaned_data['emp_id'])  
#     else:
#         form = ContractemphpclForm()

#     return render(request, 'create_employee.html', {'form': form})



# def employee_detail(request, pk):
#     employee = get_object_or_404(Contractemphpcl, pk=pk)
#     previous_employee = Contractemphpcl.objects.filter(pk__lt=pk).order_by('-pk').first()
#     next_employee = Contractemphpcl.objects.filter(pk__gt=pk).order_by('pk').first()
    
#     return render(request, 'employee_detail.html', {
#         'employee': employee,
#         'previous_employee': previous_employee,
#         'next_employee': next_employee
#     })


# def edit_employee(request, pk):
#     employee = get_object_or_404(Contractemphpcl, pk=pk)
#     # previous_employee = Contractemphpcl.objects.filter(pk__lt=pk).order_by('-pk').first()
#     # next_employee = Contractemphpcl.objects.filter(pk__gt=pk).order_by('pk').first()
#     if request.method == 'POST':
#         form = ContractemphpclForm(request.POST, instance=employee)
#         if form.is_valid():
#             employee = form.save(commit=False)
#             employee.save()
#             messages.success(request, 'Employee details updated successfully.')
#             return redirect('ContractEmployee:edit_employee', pk=form.cleaned_data['emp_id'])  
#     else:
#         form = ContractemphpclForm(instance=employee)  
#     return render(request, 'edit_employee.html', {'employee': employee,'form': form,})


# def delete_employee(request, pk):
#     Conemp = Contractemphpcl.objects.get(pk=pk)
#     if request.method == 'POST':
#         Conemp.delete()
#         return redirect('create_employee')
#     return render(request, 'delete_employee.html', {'Conemp': Conemp})
    


from django.shortcuts import render, redirect, get_object_or_404
from .forms import VendorForm, EmployeeForm, SalaryDetailsForm
from .models import Vendor, Employee, SalaryDetails

# Vendor views
def create_vendor(request):
    if request.method == 'POST':
        form = VendorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('vendor_list')
    else:
        form = VendorForm()
    return render(request, 'vendor_create.html', {'form': form})

def list_vendors(request):
    vendors = Vendor.objects.all()
    return render(request, 'vendor_list.html', {'vendors': vendors})

def update_vendor(request, ven_code):
    vendor = get_object_or_404(Vendor, ven_code=ven_code)
    form = VendorForm(request.POST or None, instance=vendor)
    if form.is_valid():
        form.save()
        return redirect('vendor_list')
    return render(request, 'vendor_update.html', {'form': form})

def delete_vendor(request, ven_code):
    vendor = get_object_or_404(Vendor, ven_code=ven_code)
    vendor.delete()
    return redirect('vendor_list')

# Employee views
def create_employee(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('employee_list')
    else:
        form = EmployeeForm()
    return render(request, 'employee_create.html', {'form': form})

def list_employees(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def update_employee(request, emp_code):
    employee = get_object_or_404(Employee, emp_code=emp_code)
    form = EmployeeForm(request.POST or None, instance=employee)
    if form.is_valid():
        form.save()
        return redirect('employee_list')
    return render(request, 'employee_update.html', {'form': form})

def delete_employee(request, emp_code):
    employee = get_object_or_404(Employee, emp_code=emp_code)
    employee.delete()
    return redirect('employee_list')

# Salary Details views
def create_salary_details(request):
    if request.method == 'POST':
        form = SalaryDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('salary_details_list')
    else:
        form = SalaryDetailsForm()
    return render(request, 'salary_details_create.html', {'form': form})

def list_salary_details(request):
    salary_details = SalaryDetails.objects.all()
    return render(request, 'salary_details_list.html', {'salary_details': salary_details})

def update_salary_details(request, salary_id):
    salary_detail = get_object_or_404(SalaryDetails, salary_id=salary_id)
    form = SalaryDetailsForm(request.POST or None, instance=salary_detail)
    if form.is_valid():
        form.save()
        return redirect('salary_details_list')
    return render(request, 'salary_details_update.html', {'form': form})

def delete_salary_details(request, salary_id):
    salary_detail = get_object_or_404(SalaryDetails, salary_id=salary_id)
    salary_detail.delete()
    return redirect('salary_details_list')
