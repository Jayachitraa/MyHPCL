from django.contrib import admin
from .models import Contractemphpcl

class ContractemphpclAdmin(admin.ModelAdmin):
    list_display = ('emp_id', 'emp_name', 'org_name', 'desg', 'doj')
    list_filter = ('org_name', 'desg', 'gender')
    search_fields = ('emp_id', 'emp_name', 'org_name')

admin.site.register(Contractemphpcl, ContractemphpclAdmin)

