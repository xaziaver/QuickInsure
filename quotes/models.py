from django.db import models
from django.conf import settings
from risks.models import Risk

class Quote(models.Model):
    risk = models.ForeignKey(Risk, on_delete=models.CASCADE)
    quote_date = models.DateTimeField(auto_now_add=True)
    quote_amount = models.DecimalField(max_digits=10, decimal_places=2)
    is_latest = models.BooleanField(default=True)