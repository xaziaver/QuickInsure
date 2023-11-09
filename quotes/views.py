from django.shortcuts import render, redirect
from .models import Quote
from risks.forms import RiskForm

def QuoteStart(request):
    return render(request, 'quotes/quote_start.html')

def QuoteSave(request):
    