from django.db import models
from django.conf import settings
from django.utils.safestring import mark_safe

from policies.models import Policy, BaseInputs, BaseOutputs


class Quote(BaseInputs, BaseOutputs, models.Model):
    bound_policy = models.OneToOneField(Policy, on_delete=models.SET_NULL, null=True, blank=True)
    start_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def display(self):
        start = self.start_date.strftime("%Y-%m-%d %H:%M")
        updated = self.update_date.strftime("%Y-%m-%d %H:%M")
        message = f'<span class="quote-id">ID: {self.number}</span>' \
                f'<span class="quote-date">Started: {start}</span>' \
                f'<span class="quote-date">Last Updated: {updated}</span>'
        return mark_safe(message)  # Use mark_safe to return HTML content