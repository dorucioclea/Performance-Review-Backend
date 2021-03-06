import django.contrib.auth.forms
from django import forms

from .models import User


class UserCreationForm(django.contrib.auth.forms.UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class UserChangeForm(django.contrib.auth.forms.UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email')


class CsvImportForm(forms.Form):
    csv_file = forms.FileField()


class CsvRowValidationForm(forms.Form):
    employee_id = forms.IntegerField(required=True)
    last_name = forms.CharField(required=True)
    first_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True)
