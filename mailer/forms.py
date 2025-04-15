from django import forms

class MailForm(forms.Form):
    email = forms.EmailField(label='Ваш email', widget=forms.EmailInput(attrs={
        'placeholder': 'Введіть вашу електронну адресу'
    }))
