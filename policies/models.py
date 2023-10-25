from django.db import models
from datetime import date

class Policy(models.Model):
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
    type = models.CharField(
        max_length=3,
        choices=TYPE_CHOICES,
        default=TYPE_CHOICES[1],
    )
    
    #coverages = 
    #forms = 
    
    #account = 

