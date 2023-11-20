from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class CoverageGroup(models.Model):
    standard_coverages = models.ForeignKey(StandardCoverages)
    additional_coverages = models.OneToMany(AdditionalCoverages)

class CoverageGroupLink(models.Model):
    # generic coverage table key (key for Coverage A, Coverage B, )
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')


class BaseCoverage(models.Model):
    # Base model for all coverage types
    coverage_group = models.ForeignKey(CoverageGroup, on_delete=models.CASCADE, related_name='coverages')
    amount = models.PositiveIntegerField()
    
    class Meta:
        abstract = True

class StandardCoverage(BaseCoverage):
    # fields that apply to all standard coverages
    class Meta:
        abstract = True

class CoverageA(StandardCoverage):
    # fields specific to Coverage A

class CoverageB(StandardCoverage):
    # fields specific to Coverage B


class AdditionalCoverage(BaseCoverage):
     # fields that apply to all additional coverages
     class Meta:
        abstract = True

class HomeSystemBreakdown(AdditionalCoverage):
# fields specific to Home System Breakdown coverage