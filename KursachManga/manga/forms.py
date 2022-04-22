from django import forms
from .models import *


class AddTitlesForm(forms.Form):
    name = forms.CharField(max_length=120,)
    descriptions = forms.CharField(max_length=120,)
    genre = forms.CharField(max_length=120,)
    author = forms.CharField(max_length=120,)
    publisher = forms.CharField(max_length=120,)
    translator = forms.CharField(max_length=120,)
    slug = forms.SlugField(max_length=120)

    def __str__(self):
        return self.name
