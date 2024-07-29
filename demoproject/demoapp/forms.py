from django import forms
from django.forms.widgets import NumberInput

class loginForm(forms.Form):
    email = forms.EmailField(label="Enter email address")
    start_date = forms.DateField(widget=NumberInput(attrs={'type':'date'}))