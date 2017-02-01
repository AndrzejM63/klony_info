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
        fields = ['uid', 'botanic_name', 'latin_name', 'other_names', 'origin1', 'origin2', 'occurrence', 'height_max1', \
                  'height_max1', 'shape1', 'shape2', 'leaf_structure', 'leaf_size',  \
                  'new_image_tree', 'new_image_bark', 'new_image_leaf']

class AcersSearchForm(forms.Form):
    b_uid = forms.CharField(required=False)
    l_uid = forms.CharField(required=False)
    shape = forms.CharField(required=False)
    frost = forms.CharField(required=False)
    lc_summer = forms.CharField(required=False)
    lc_autumn = forms.CharField(required=False)

    # botanic_name = forms.CharField(max_length=113, required=False)
    # latin_name = forms.CharField(max_length=113, required=False)

