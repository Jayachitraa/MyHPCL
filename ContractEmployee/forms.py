from django import forms
from .models import Contractemphpcl

class ContractemphpclForm(forms.ModelForm):
    class Meta:
        model = Contractemphpcl
        fields = '__all__'
