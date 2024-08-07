from django import forms

class RegisterForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget = forms.PasswordInput())
    passRepeat = forms.CharField(widget = forms.PasswordInput())
