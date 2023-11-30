from django import forms
from .models import Vendor, Employee, SalaryDetails

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class SalaryDetailsForm(forms.ModelForm):
    class Meta:
        model = SalaryDetails
        fields = '__all__'
 