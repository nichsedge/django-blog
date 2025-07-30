"""
from django import forms
from .models import Akun

class AkunForm(forms.ModelForm):
    class Meta:
        model = Akun
        fields = '__all__'
        widgets = {
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'type': 'email',
                'id': 'email',
                'placeholder': 'Masukkan email...'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'type': 'name',
                'id': 'name',
                'placeholder': 'Masukkan name...'
            }),
            'password': forms.PasswordInput(attrs={
                'class': 'form-control',
                'type': 'password',
                'id': 'password',
                'placeholder': 'Masukkan password...'
            }),
            
        }
"""
