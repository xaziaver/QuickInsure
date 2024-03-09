# TODO: implement rating app
# TODO: setup quote tracking


from django.db import models
from django.conf import settings
from django.utils.safestring import mark_safe
from django.contrib.contenttypes.fields import GenericRelation
from datetime import date


class BaseInput(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # input/output objects
    coverage = GenericRelation('coverages.Coverage')
    rating = GenericRelation('rating.Rating')
    form = GenericRelation('forms.Form')
    
    effective_date = models.DateField(default=date.today)
    expiration_date = models.DateField(null=True)
    
    PRODUCT_CHOICES = [
        ("HOME", "Homeowner's Insurance"),
        ("RENT", "Renter's Insurance")
    ]
    TYPE_CHOICES = [
        ("HO3", "HO3"),
        ("HO4", "HO4"),
        ("HO6", "HO6")
    ]

    product = models.CharField(
        max_length=25,
        choices=PRODUCT_CHOICES,
        default=PRODUCT_CHOICES[1][0],
    )

    policy_type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        default=TYPE_CHOICES[1][0],
    )

    class Meta:
        abstract = True


class BaseOutput(models.Model):
    premium = models.DecimalField(max_digits=10, decimal_places=2, null=True, default=None)
    status = models.CharField(max_length=10, null=False)
    number = models.CharField(max_length=25, null=False)

    class Meta:
        abstract = True


class Quote(BaseInput, BaseOutput):
    start_date = models.DateTimeField(auto_now_add=True, null=False)
    update_date = models.DateTimeField(auto_now=True, null=False)
    # if a quote is bound this is the assigned policy
    bound_policy = models.OneToOneField('policies.Policy', on_delete=models.SET_NULL, null=True, blank=True)

    ### TRACKING ### ---> probably will move to analytics

    # error collection process undefined, but
    # this will hold references to all errors during quoting
    #error_refs =

    # feedback the user can send, update, 
    # and see status/replices to feedback
    #feedback =

    # time to provide a premium quote to user
    #t_to_rate =

    # eventually want a way to quickly jump into the quoting process before setting up and account
    # and this will be important for tracking where the users are coming from
    #referral_source =

    ################

    # returns HTML description of the Quote
    def display(self):
        start = self.start_date.strftime("%Y-%m-%d %H:%M")
        updated = self.update_date.strftime("%Y-%m-%d %H:%M")
        message = f'<span class="quote-id">Quote ID: {self.number}</span>' \
                f'<span class="quote-date">Started: {start}</span>' \
                f'<span class="quote-date">Last Updated: {updated}</span>'

        return mark_safe(message)