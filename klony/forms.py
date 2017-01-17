from django import forms
from django.forms import ModelForm

from klony.models import Acers


class LoginForm(forms.Form):
    login = forms.CharField(
        label='Podaj login',
        max_length=32,
        # widget=forms.Textarea,
        widget=forms.TextInput,
        required=True,
    )
    password = forms.CharField(
        label='Hasło',
        max_length=32,
        required=True,
        widget=forms.PasswordInput,
    )


class AcersMainForm(ModelForm):
    class Meta:
        model = Acers
        fields = ['botanic_name', 'latin_name', 'image_tree', 'new_image_tree', 'new_image_bark', 'new_image_leaf']
