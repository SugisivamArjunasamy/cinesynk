from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)

class SearchForm(forms.Form):
    searchInput = forms.CharField(label="searchInput", required=True)

class RegistrationForm(forms.Form):
    email = forms.EmailField(label='email', required=True)
    username = forms.CharField(label='username', required=True)
    password = forms.CharField(label='password', widget=forms.PasswordInput, required=True)
    confirmpassword = forms.CharField(label='confirmPassword', widget=forms.PasswordInput, required=True)

class MessageForm(forms.Form):
    message = forms.CharField(label="message", required=True)
    recipient_email = forms.CharField(label='recipient_email', required=True)