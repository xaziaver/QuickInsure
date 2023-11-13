from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET
from common.decorators import htmx_required

from .models import Quote
from risks.models import Risk
from policies.models import Policy

from risks.forms import RiskForm

def QuoteStart(request):
    new_quote = Quote.objects.create()

    context = {
        'new_quote_id': new_quote.id,
    }

    return render(request, 'quotes/quote_start.html', context)

def QuoteSave(request):
    return render(request, 'quotes/quote_start.html')

@htmx_required
@require_GET
# from quote_start.html
def QuoteViewBasic(request, quote_id):
    quote = Quote.objects.get(id=quote_id)
    return render(request, 'quotes/quote_basic.html', {'quote': quote})