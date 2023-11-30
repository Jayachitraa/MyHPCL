from django.db import models


class Vendor(models.Model):
    ven_code = models.AutoField(primary_key=True)
    ven_name = models.CharField(max_length=100)
    ven_addr1 = models.CharField(max_length=100, blank=True, null=True)
    ven_addr2 = models.CharField(max_length=100, blank=True, null=True)
    ven_addr3 = models.CharField(max_length=100, blank=True, null=True)
    ven_mob = models.CharField(max_length=15, blank=True, null=True)
    ven_email = models.EmailField(max_length=100, blank=True, null=True)
    ven_adhar = models.CharField(max_length=20, blank=True, null=True)
    ven_bank_det = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.ven_name



class Employee(models.Model):
    emp_code = models.AutoField(primary_key=True)
    emp_name = models.CharField(max_length=100)
    emp_dob = models.DateField(blank=True, null=True)
    emp_qualification = models.CharField(max_length=20, blank=True, null=True)
    emp_organization = models.CharField(max_length=100, blank=True, null=True)
    emp_designation = models.CharField(max_length=50, blank=True, null=True)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    emp_basic_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    emp_doj = models.DateField(blank=True, null=True)
    emp_gender = models.CharField(max_length=10, blank=True, null=True)
    emp_address1 = models.CharField(max_length=100, blank=True, null=True)
    emp_address2 = models.CharField(max_length=100, blank=True, null=True)
    emp_pin_code = models.CharField(max_length=20, blank=True, null=True)
    emp_mobile = models.CharField(max_length=15, blank=True, null=True)
    emp_email = models.EmailField(max_length=100, blank=True, null=True)
    emp_esic_enrolled = models.CharField(max_length=20, blank=True, null=True)
    emp_esic_location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.emp_name




class SalaryDetails(models.Model):
    salary_id = models.AutoField(primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    basic_salary = models.DecimalField(max_digits=10, decimal_places=2)
    allowances = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    deductions = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    net_salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f"Salary Details for {self.employee.emp_name}"
