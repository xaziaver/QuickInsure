from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import UpdateView
from django.views.decorators.http import require_GET
from common.decorators import htmx_required

from .models import Quote
from .forms import BasicDetailForm
from risks.models import Risk
from risks.forms import RiskForm
from policies.models import Policy
from coverages.models import CoverageGroup
from coverages.forms import CoverageDetailForm
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

        # associate new quote with new input groups
        new_quote.latest_coverage_group = new_coverage_group
        new_quote.latest_claim_group = new_claim_group
        new_quote.latest_form_group = new_form_group
        new_quote.save()

        context = {
            'new_quote': new_quote,
            'new_coverage_group': new_coverage_group,
            'new_claim_group': new_claim_group,
            'new_form_group': new_form_group,
        }

        return render(request, 'quotes/quote_start.html', context)
    else:
        return redirect('/')  

def QuoteResume(request, quote_id):
    quote = get_object_or_404(Quote, id=quote_id)
    
    # use same names as QuoteStart to match html page
    context = {
        'new_quote': quote,
        'new_coverage_group': quote.latest_coverage_group,
        'new_claim_group': quote.latest_claim_group,
        'new_form_group': quote.latest_form_group,
    }

    return render(request, 'quotes/quote_start.html', context)

def QuoteSave(request, quote_id):
    if request.method == 'POST':
        # Fetch the existing Quote object
        quote = Quote.objects.get(id=quote_id)

        # Process each form based on its type
        for key, value in request.POST.lists():
            if key == 'form_type':
                for form_type in value:
                    if form_type == 'basic':
                        # Process basic form data
                        basic_data = {k: v for k, v in request.POST.items() if k != 'form_type'}
                        basic_form = BasicDetailForm(basic_data, instance=quote)
                        if basic_form.is_valid():
                            basic_form.save()
                    '''
                    elif form_type == 'coverage':
                        # Process coverage form data
                        coverage_data = {k: v for k, v in request.POST.items() if k != 'form_type'}
                        coverage_form = CoverageDetailForm(coverage_data, instance=quote.latest_coverage_group)
                        if coverage_form.is_valid():
                            coverage_form.save()
                    '''
        # ... continue for other forms

        message = "Data saved successfully"
        return render(request, 'quotes/_quote_save_status.html', {'message': message})

    # Handle non-POST requests here


@htmx_required
@require_GET
# from quote_start.html
def QuoteViewBasic(request, quote_id):
    quote = Quote.objects.get(id=quote_id)
    return render(request, 'quotes/quote_basic.html', {'quote': quote})


class BasicDetailView(UpdateView):
    model = Quote
    form_class = BasicDetailForm
    template_name = 'quotes/quote_basic_form.html'
    success_url = reverse_lazy('home')