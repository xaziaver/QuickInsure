from django import forms
from .models import Quote

class BasicDetailForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BasicDetailForm, self).__init__(*args, **kwargs)
        
        # if existing instance
        if self.instance.pk: 
            # expiration_date dynamic updates
            self.fields['expiration_date'].disabled = True
            # trigger update on term field change
            self.fields['term'].widget.attrs.update({
                'hx-get': '/quotes/update_exp_date/',
                'hx-trigger': 'change',
                'hx-swap': 'outerHTML',
                'hx-target': '#expiration_date_container',
                'hx-include': '#id_effective_date',
            })
            # trigger update on effective date change
            self.fields['effective_date'].widget.attrs.update({
                'hx-get': '/quotes/update_exp_date/',
                'hx-trigger': 'change',
                'hx-swap': 'outerHTML',
                'hx-target': '#expiration_date_container',
                'hx-include': '#id_term',
            })

    class Meta:
        model = Quote
        fields = ['product', 'policy_type', 'term', 'effective_date', 'expiration_date']
        
        # dates are being set as input type 'text' when form is rendered
        # so setting explictly here to get 'date' types
        widgets = {
            'effective_date': forms.DateInput(attrs={'type': 'date'}),
            'expiration_date': forms.DateInput(attrs={'type': 'date'}),
        }