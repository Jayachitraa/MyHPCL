# # from django.contrib import admin
# # from .models import Contractemphpcl

# # class ContractemphpclAdmin(admin.ModelAdmin):
# #     list_display = ('emp_id', 'emp_name', 'org_name', 'desg', 'doj')
# #     list_filter = ('org_name', 'desg', 'gender')
# #     search_fields = ('emp_id', 'emp_name', 'org_name')

# # admin.site.register(Contractemphpcl, ContractemphpclAdmin)

from django.contrib import admin
from .models import Vendor, Employee, SalaryDetails

@admin.register(Vendor)
class VendorAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Vendor._meta.fields]

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Employee._meta.fields]

@admin.register(SalaryDetails)
class SalaryDetailsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in SalaryDetails._meta.fields]

