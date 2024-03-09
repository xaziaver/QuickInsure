from django.db import models

# TODO: implement binding process and initial "New Business" transaction

class Transaction(models.Model):
    # history = 
    policy = models.ForeignKey('policies.Policy', on_delete=models.CASCADE)
    status = models.CharField(max_length=10)
    transaction_date = models.DateTimeField(auto_now_add=True)
    notes = models.CharField(max_length=100)

    # if any change between current transaction and previous
    premium_change = models.DecimalField(max_digits=10, decimal_places=2)

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

# snapshot of data associated with policy for each transaction
# class History(models.Model):
#    risk =
#    coverage =
#    rating =
#    form =
#    claim =