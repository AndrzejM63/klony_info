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
        fields = ['uid', 'botanic_name', 'latin_name', 'other_names', 'origin1', 'origin2', 'occurrence', 'height_max1',
                  'height_max1', 'shape1', 'shape2', 'leaf_structure', 'leaf_size',
                  'new_image_tree', 'new_image_bark', 'new_image_leaf']


class AcersSearchForm(forms.Form):
    b_uid = forms.CharField(required=False)
    l_uid = forms.CharField(required=False)
    shape = forms.CharField(required=False)
    frost = forms.CharField(required=False)
    lc_summer = forms.CharField(required=False)
    lc_autumn = forms.CharField(required=False)


class AcersSingleForm(forms.Form):
    botanic_name_variant = forms.CharField(max_length=204, required=False)
    other_names = forms.CharField(max_length=113, required=False)
    latin_name = forms.CharField(max_length=113, required=False)
    description = forms.CharField(widget=forms.Textarea, required=False)
    origin = forms.CharField(max_length=113, required=False)
    occurrence = forms.CharField(max_length=113, required=False)
    max_height = forms.CharField(max_length=113, required=False )
    shape = forms.CharField(max_length=204, required=False)
    leaf_structure = forms.CharField(max_length=204, required=False)
    leaf_size = forms.CharField(max_length=113, required=False)
    leaf_spring = forms.CharField(max_length=204, required=False)
    leaf_summer = forms.CharField(max_length=204, required=False)
    leaf_autumn = forms.CharField(max_length=204, required=False)
    leaf_tail = forms.CharField(max_length=150, required=False)
    bark = forms.CharField(max_length=204, required=False)
    flowers = forms.CharField(max_length=204, required=False)
    fruits = forms.CharField(max_length=204, required=False)
    frost_res = forms.CharField(max_length=204, required=False)
    frost_zone = forms.CharField(max_length=8, required=False)
    stand = forms.CharField(max_length=204, required=False)
    soil_kind = forms.CharField(max_length=75, required=False)
    soil_ph = forms.CharField(max_length=75, required=False)
    image_tree = forms.ImageField(required=False)
    image_bark = forms.ImageField(required=False)
    image_leaf = forms.ImageField(required=False)
    characteristics = forms.CharField(max_length=204, required=False)
    poland_availability = forms.CharField(max_length=8, required=False)
