from django import forms
from .models import Item


class ItemForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = ['name', 'done']
