from django import forms
from .models import *


class AddTitlesForm(forms.ModelForm):
    class Meta:
        model = Titles
        fields = ['name', 'descriptions', 'poster', 'genre', 'author', 'publisher', 'translator', 'slug']
