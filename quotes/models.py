from django.db import models
from django.conf import settings

#from policies.models import BaseInputs


class Quote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    risk = models.ForeignKey('Risk', on_delete=models.CASCADE)
    bound_policy = models.OneToOneField('Policy', on_delete=models.SET_NULL, null=True, blank=True)
    
    #quote_inputs = models.OneToOneField(BaseInputs, on_delete=models.CASCADE)
    quote_date = models.DateTimeField(auto_now_add=True)
    quote_premium = models.DecimalField(max_digits=10, decimal_places=2)
    is_bound = models.BooleanField(default=True)