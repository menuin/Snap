from django import forms
from .models import Couple

class NameForm(forms.ModelForm):

    class Meta:
        model=Couple
        fields=['name']