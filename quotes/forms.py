from django import forms
from .models import Quote

class BasicDetailForm(forms.ModelForm):
    class Meta:
        model = Quote
        fields = ['effective_date', 'expiration_date', 'product', 'policy_type']
        # Add any other fields you need