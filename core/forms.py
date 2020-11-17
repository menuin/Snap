from django import forms
from .models import Couple

class MoveForm(forms.ModelForm):

    class Meta:
        model=Couple
        fields=['name','photo']

