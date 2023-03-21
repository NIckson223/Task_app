from .models import Task
from django import forms
from django.forms import ModelForm, TextInput, Textarea, DateInput


class TaskForm(ModelForm):
    class DateInput(forms.DateInput):
        input_type = 'date'

    class Meta:
        model = Task
        fields = ['title', 'description', 'date', 'date_end']
        widgets = {
            'title': TextInput(attrs={
                'class': 'input_name input',
                'placeholder': 'Input task name'
            }),
            'description': Textarea(attrs={
                'class': 'input_description input',
            }),
            'date': DateInput(attrs={
                'class': 'input input_date',
            }),
            'date_end': DateInput(attrs={
                'class': 'input input_date',
            }),
        }
