from django.shortcuts import render, redirect,get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import ContractemphpclForm
from .models import Contractemphpcl

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('create_employee') 
        else:
           return render(request, 'login.html', {'error': 'Invalid username or password'})

    return render(request, 'login.html')


def create_employee(request):
    if request.method == 'POST':
        form = ContractemphpclForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Employee details submitted successfully.')  
            return redirect('ContractEmployee:employee_detail', pk=form.cleaned_data['emp_id'])  
    else:
        form = ContractemphpclForm()

    return render(request, 'create_employee.html', {'form': form})



def employee_detail(request, pk):
    employee = get_object_or_404(Contractemphpcl, pk=pk)
    previous_employee = Contractemphpcl.objects.filter(pk__lt=pk).order_by('-pk').first()
    next_employee = Contractemphpcl.objects.filter(pk__gt=pk).order_by('pk').first()
    
    return render(request, 'employee_detail.html', {
        'employee': employee,
        'previous_employee': previous_employee,
        'next_employee': next_employee
    })


def edit_employee(request, pk):
    employee = get_object_or_404(Contractemphpcl, pk=pk)
    previous_employee = Contractemphpcl.objects.filter(pk__lt=pk).order_by('-pk').first()
    next_employee = Contractemphpcl.objects.filter(pk__gt=pk).order_by('pk').first()
    if request.method == 'POST':
        form = ContractemphpclForm(request.POST, instance=employee)
        if form.is_valid():
            employee = form.save(commit=False)
            employee.save()
            messages.success(request, 'Employee details updated successfully.')
            return redirect("create_employee")  
    else:
        form = ContractemphpclForm(instance=employee)  # Moved this line inside the else block

    return render(request, 'edit_employee.html', {'employee': employee,'form': form,'previous_employee': previous_employee,'next_employee': next_employee})


def delete_employee(request, pk):
    Conemp = Contractemphpcl.objects.get(pk=pk)
    if request.method == 'POST':
        Conemp.delete()
        return redirect('create_employee')
    return render(request, 'delete_employee.html', {'Conemp': Conemp})
    


