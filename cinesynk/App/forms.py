from django import forms

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email', required=True)
    password = forms.CharField(label='Password', widget=forms.PasswordInput, required=True)

class SearchForm(forms.Form):
    searchInput = forms.CharField(label="searchInput", required=True)