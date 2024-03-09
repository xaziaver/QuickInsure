from django import forms
from .models import Coverage

class CoverageDetailForm(forms.ModelForm):
    class Meta:
        model = Coverage
        fields = ['id', 'object_id', 'save_test']