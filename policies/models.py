from django.db import models
from django.conf import settings

from quotes.models import BaseInput, BaseOutput

# TODO: set up accounts app and link
# TODO: set up UW app and link
# TODO: set up billing app and link

class Policy(BaseInput, BaseOutput):
    
    #claim = models.ForeignKey('claims.Claim', on_delete=models.SET_NULL, null=True)

    # holds the current term of the policy
    current_term = models.PositiveSmallIntegerField(null=True)
    
    # parties associated with the policy
    # e.g.. the user, Mortgagee, Lienholder and others added on the policy
    # account = 

    # Underwriting object to hold other details
    # related to the underwriting process
    # UW = 

    # billing object for payments
    # billing = 