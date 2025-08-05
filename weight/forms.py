from django import forms 
from authentication.models import CustomUser
from .models import WeightEntry

class WeightUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['weight']
        widgets = {
            'weight': forms.NumberInput(attrs={'step': '0.1', 'placeholder': 'Введите ваш вес (кг)'}),
        }

class WeightEntryForm(forms.ModelForm):
    class Meta:
        model = WeightEntry
        fields = ['weight']
        widgets = {
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите ваш вес (кг)'})
        }
