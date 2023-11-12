from django.db import models
from django.conf import settings
from datetime import date


class Policy(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    risk = models.ForeignKey('Risk', on_delete=models.CASCADE)
    originating_quote = models.OneToOneField('Quote', on_delete=models.SET_NULL, null=True, blank=True)
    
    #policy_inputs = models.OneToOneField(BaseInputs, on_delete=models.CASCADE)
    premium = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=100)

'''class BaseInputs(models.Model):
    effective_date = models.DateField(default=date.today)
    expiration_date = models.DateField()

    PRODUCT_CHOICES = [
        ("HOME", "Homeowner's Insurance"),
        ("RENT", "Renter's Insurance")
    ]
    TYPE_CHOICES = [
        ("HO3", "HO3"),
        ("HO4", "HO4"),
        ("HO6", "HO6")
    ]

    product = models.CharField(
        max_length=25,
        choices=PRODUCT_CHOICES,
        default=PRODUCT_CHOICES[1],
    )

    policy_type = models.CharField(
        max_length=3,
        choices=TYPE_CHOICES,
        default=TYPE_CHOICES[1],
    )
    
    #coverages = 
    #forms = 
    #account = 
    '''