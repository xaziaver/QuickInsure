from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class CoverageGroup(models.Model):
    # Generic foreign key setup - points to either a Quote object or Policy object
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

class CoverageType(models.Model):
    
    COVERAGE_NAMES = [
        ("A", "Coverage A"),
        ("B", "Coverage B"),
        ("C", "Coverage C"),
    ]
    name = models.CharField(
        max_length=25,
        choices=COVERAGE_NAMES,
    )
    
    amount = models.PositiveIntegerField()

class CoverageInstance(models.Model):
    coverage_type = models.ForeignKey(CoverageType, on_delete=models.CASCADE)

class CoverageTransactionLink(models.Model):
    coverage_group = models.ForeignKey(CoverageGroup, on_delete=models.CASCADE)
    coverage_instance = models.ForeignKey(CoverageInstance, on_delete=models.CASCADE)