from django import forms
from .models import AppointmentsList, MessageTemplate

# -------------------------------
# 1. Form for Creating an Appointment List
# -------------------------------
class AppointmentsListForm(forms.ModelForm):
    csv_file = forms.FileField(
        required=True,
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
            'accept': '.csv'
        })
    )

    class Meta:
        model = AppointmentsList
        fields = ['title', 'message_selected', 'csv_file']

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter list name...'
            }),
            'message_selected': forms.SelectMultiple(attrs={
                'class': 'form-control'
            }),
        }

# -------------------------------
# 2. Form for Creating Message Templates
# -------------------------------
class MessageTemplateForm(forms.ModelForm):
    class Meta:
        model = MessageTemplate
        fields = ['category', 'content']

        widgets = {
            'category': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter message category...'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Enter message content...'
            }),
        }
