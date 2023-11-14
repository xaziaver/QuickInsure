from django.db import models
from django.conf import settings
from datetime import date


class BaseInputs(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    risk = models.ForeignKey('risks.Risk', on_delete=models.SET_NULL, null=True)
    latest_coverage_group = models.ForeignKey('coverages.CoverageGroup', on_delete=models.SET_NULL, null=True)
    latest_claim_group = models.ForeignKey('claims.ClaimGroup', on_delete=models.SET_NULL, null=True)
    latest_form_group = models.ForeignKey('forms.FormGroup', on_delete=models.SET_NULL, null=True)
    
    effective_date = models.DateField(default=date.today)
    expiration_date = models.DateField(null=True)

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
        default=PRODUCT_CHOICES[1][0],
    )

    policy_type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        default=TYPE_CHOICES[1][0],
    )

    class Meta:
        abstract = True

class BaseOutputs(models.Model):
    premium = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    status = models.CharField(max_length=10, null=True)
    number = models.CharField(max_length=25, null=True)

    class Meta:
        abstract = True

class Policy(BaseInputs, BaseOutputs, models.Model):
    originating_quote = models.OneToOneField('quotes.Quote', on_delete=models.SET_NULL, null=True, blank=True)
    term = models.PositiveSmallIntegerField(null=True)