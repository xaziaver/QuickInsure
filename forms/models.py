from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# TODO: separate forms for Quote and Policy... quotes will have
#       minimal forms associated (application, quote sheet)
# TODO: add fields common to all types of forms in Form

class Form(models.Model):
    # Generic foreign key setup - points to either a Quote object or Policy object
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')