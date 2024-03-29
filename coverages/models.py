from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# TODO: continue with defining types of coverages and deciding on how the 
#       inheritance and table setups should work to allow for variability, 
#       future expansion and easy updates

class Coverage(models.Model):
    # connected to a Quote or Policy object
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    # input fields
    save_test = models.CharField(max_length=10)

'''
class CoverageGroupLink(models.Model):
    coverage_group = models.ForeignKey(CoverageGroup, on_delete=models.CASCADE, related_name='coverage_links')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

class BaseCoverage(models.Model):
    amount = models.PositiveIntegerField()
    
    class Meta:
        abstract = True

class StandardCoverage(BaseCoverage):
    pass

    class Meta:
        abstract = True

class CoverageA(StandardCoverage):
    details = models.CharField(max_length=255)

class CoverageB(StandardCoverage):
    details = models.CharField(max_length=255)

class AdditionalCoverage(BaseCoverage):
    pass 
    
    class Meta:
        abstract = True

class HomeSystemBreakdown(AdditionalCoverage):
    details = models.CharField(max_length=255)
'''