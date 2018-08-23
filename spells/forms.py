from django import forms
from . import models

class CreateSpell(forms.ModelForm):
    class Meta:
        model = models.Spell
        fields = ['spell_name','slug','description','incantation','purpose','type','reference','extract','extract_author','image']

