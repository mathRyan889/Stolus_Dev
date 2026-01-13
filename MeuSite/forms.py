from django import forms
from .models import Lead

class LeadForm(forms.ModelForm):
    class Meta:
        model = Lead
        fields = ['name', 'email', 'phone']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Seu nome',
                'class': 'input'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Seu email',
                'class': 'input'
            }),
            'phone': forms.TextInput(attrs={
                'placeholder': 'Seu WhatsApp',
                'class': 'input'
            }),
        }
