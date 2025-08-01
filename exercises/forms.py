from django import forms
from .models import Exercise

class ExercisesForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'muscle_group', 'equipment', 'type']


