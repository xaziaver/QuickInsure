from django.shortcuts import render
from .models import Quote
from risks.models import Risk

def QuoteStart(request):
    user_risks = Risk.objects.filter(user_id=request.user.id)
    return render(request, 'quotes/quote_start.html', {'risks': user_risks})