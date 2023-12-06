from django import forms


class LogInForm(forms.Form):
    email = forms.EmailField(label="Email Address", max_length=50)
    password = forms.CharField(label="Password", max_length=30)