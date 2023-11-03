from django.shortcuts import render
from .models import Quote

def QuoteStart(request):
    return render(request, 'quotes/quote_start.html')