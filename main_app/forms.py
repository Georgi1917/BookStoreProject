from django import forms

from main_app.models import User


class LogInForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password']