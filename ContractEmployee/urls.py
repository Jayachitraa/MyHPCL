from django.urls import path
from . import views

app_name = 'ContractEmployee'

urlpatterns = [
    # ... other URL patterns ...
    path('login/', views.login_view, name='login'),
    path('create_employee/', views.create_employee, name='create_employee'),
    path('detail_employee/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('edit_employee/<int:pk>/', views.edit_employee, name='edit_employee'),
    path('delete/<int:pk>/', views.delete_employee, name='delete_employee'),
    
]