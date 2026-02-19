from django import forms
from apps.shops_app.models import User







class UserForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )
    email = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
        })
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
        })
    )

    password_confirm = forms.CharField(
        label="Parolni tasdiqlang",
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = User
        fields = ['first_name', 'username', 'email', 'password']



class LoginForm(forms.Form):
    username = forms.CharField(label="Foydalanuvchi nomi", widget=forms.TextInput(attrs={'class': "form-input"}))
    password = forms.CharField(label="Parolingizni kiriting", widget=forms.PasswordInput(attrs={'class': "form-input"}))


