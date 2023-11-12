from django.shortcuts import render, redirect

from .models import Quote
from risks.models import Risk
from policy.models import Policy

from risks.forms import RiskForm

def QuoteStart(request):
    new_quote = Quote.objects.create()
    new_policy = Policy.objects.create()

    return render(request, 'quotes/quote_start.html')

def QuoteSave(request):
    