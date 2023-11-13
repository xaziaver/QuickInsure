from django.db import models


class Transaction(models.Model):
    policy = models.ForeignKey('policies.Policy', on_delete=models.CASCADE)
    coverage_group = models.ForeignKey('coverages.CoverageGroup', on_delete=models.SET_NULL, null=True)
    claim_group = models.ForeignKey('claims.ClaimGroup', on_delete=models.SET_NULL, null=True)
    form_group = models.ForeignKey('forms.FormGroup', on_delete=models.SET_NULL, null=True)

    status = models.CharField(max_length=10)
    transaction_date = models.DateTimeField(auto_now_add=True)
    premium_change = models.DecimalField(max_digits=10, decimal_places=2)
    notes = models.CharField(max_length=100)

    TRANSACTION_TYPES = [
        ("NB", "New Business"),
        ("RN", "Renewal"),
        ("END", "Endorsement"),
        ("I", "Information"),
        ("C", "Cancel"),
    ]

    transaction_type = models.CharField(
        max_length=5,
        choices=TRANSACTION_TYPES,
    )