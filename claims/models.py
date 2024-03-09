from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


# TODO: define types of claims based on product choice
# TODO: add fields pertinent to all claim types in Claim object
# TODO: differentiate between pre-existing claims and claims while policy is active

class Claim(models.Model):
    policy = models.ForeignKey('policies.Policy', related_name='claims', on_delete=models.SET_NULL, null=True, blank=True)