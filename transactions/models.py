from django.db import models

class Transaction(models.Model):
    policy = models.ForeignKey('Policy', on_delete=models.CASCADE)
