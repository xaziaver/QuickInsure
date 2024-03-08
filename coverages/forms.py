from django import forms
from .models import CoverageGroup

class CoverageDetailForm(forms.ModelForm):
    class Meta:
        model = CoverageGroup
        fields = ['id', 'object_id']