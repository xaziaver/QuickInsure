from django.db import models
from django.conf import settings

from policies.models import Policy, BaseInputs, BaseOutputs


class Quote(BaseInputs, BaseOutputs, models.Model):
    bound_policy = models.OneToOneField(Policy, on_delete=models.SET_NULL, null=True, blank=True)
    start_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now_add=True)

    def display(self):
        message = "ID: " + self.number + \
                ", Started: " + str(self.start_date) + \
                ", Last Updated: " + str(self.update_date)
        return message