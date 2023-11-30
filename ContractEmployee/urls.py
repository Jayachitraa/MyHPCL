# from django.urls import path
# from . import views

# app_name = 'ContractEmployee'

# urlpatterns = [
#     path('login/', views.login_view, name='login'),
#     path('create_employee/', views.create_employee, name='create_employee'),
#     path('detail_employee/<int:pk>/', views.employee_detail, name='employee_detail'),
#     path('edit_employee/<int:pk>/', views.edit_employee, name='edit_employee'),
#     path('delete/<int:pk>/', views.delete_employee, name='delete_employee'),
    
# ]


from django.urls import path
from . import views

urlpatterns = [
    # Vendor URLs
    path('vendor/create/', views.create_vendor, name='vendor_create'),
    path('vendor/list/', views.list_vendors, name='vendor_list'),
    path('vendor/update/<int:ven_code>/', views.update_vendor, name='vendor_update'),
    path('vendor/delete/<int:ven_code>/', views.delete_vendor, name='vendor_delete'),

    # Employee URLs
    path('employee/create/', views.create_employee, name='employee_create'),
    path('employee/list/', views.list_employees, name='employee_list'),
    path('employee/update/<int:emp_code>/', views.update_employee, name='employee_update'),
    path('employee/delete/<int:emp_code>/', views.delete_employee, name='employee_delete'),

    # Salary Details URLs
    path('salary_details/create/', views.create_salary_details, name='salary_details_create'),
    path('salary_details/list/', views.list_salary_details, name='salary_details_list'),
    path('salary_details/update/<int:salary_id>/', views.update_salary_details, name='salary_details_update'),
    path('salary_details/delete/<int:salary_id>/', views.delete_salary_details, name='salary_details_delete'),
]
