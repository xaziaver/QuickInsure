from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.views.decorators.http import require_GET
from common.decorators import htmx_required

from .models import Quote
from .forms import BasicDetailForm
from risks.models import Risk
from risks.forms import RiskForm
from policies.models import Policy
from coverages.models import CoverageGroup
from claims.models import ClaimGroup
from forms.models import FormGroup




def QuoteStart(request):
    # check that user is authenticated
    if request.user.is_authenticated:
        # create new quote and input groups
        new_quote = Quote.objects.create(user=request.user) 
        new_coverage_group = CoverageGroup.objects.create(content_object=new_quote)
        new_claim_group = ClaimGroup.objects.create(content_object=new_quote)
        new_form_group = FormGroup.objects.create(content_object=new_quote)

        context = {
            'new_quote': new_quote,
            'new_coverage_group': new_coverage_group,
            'new_claim_group': new_claim_group,
            'new_form_group': new_form_group,
        }

        return render(request, 'quotes/quote_start.html', context)
    else:
        return redirect('/')  


def QuoteSave(request):
    return render(request, 'quotes/quote_start.html')

@htmx_required
@require_GET
# from quote_start.html
def QuoteViewBasic(request, quote_id):
    quote = Quote.objects.get(id=quote_id)
    return render(request, 'quotes/quote_basic.html', {'quote': quote})

class BasicDetailView(CreateView):
    model = Quote
    form_class = BasicDetailForm
    template_name = 'quotes/quote_basic_form.html'
    success_url = reverse_lazy('home')