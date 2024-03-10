# TODO: add rating object as an input group
# TODO: add other forms from quote pages to QuoteSave() 
#       and iterate to save data into appropriate data models
# TODO: update QuoteSave() to handle non-POST requests to save without submitting


from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import UpdateView
from django.views.decorators.http import require_GET
from common.decorators import htmx_required
from django.http import JsonResponse
from datetime import datetime, timedelta

from .models import Quote
from risks.models import Risk
from coverages.models import Coverage
from rating.models import Rating
from forms.models import Form

from .forms import BasicDetailForm
from risks.forms import RiskForm
from coverages.forms import CoverageDetailForm

# start a new quote from the home page
def QuoteStart(request):
    # check that user is authenticated
    if request.user.is_authenticated:

        # create new quote and initialize fields
        new_quote_obj = Quote.objects.create(user=request.user)
        new_quote_obj.number = generate_quote_number(new_quote_obj)
        new_quote_obj.status = 'New'

        # create input/output objects
        new_coverage_obj = Coverage.objects.create(content_object=new_quote_obj)
        new_rating_obj = Rating.objects.create(content_object=new_quote_obj)
        new_form_obj = Form.objects.create(content_object=new_quote_obj)

        new_quote_obj.save()
        
        # objects to be passed to the quote landing page
        context = {
            'new_quote': new_quote_obj,
            'new_coverage': new_coverage_obj,
            'new_rating': new_rating_obj,
            'new_form': new_form_obj,
        }
        return render(request, 'quotes/start.html', context)
    else:
        return redirect('/')  

# resume a previously saved quote from the home page
def QuoteResume(request, quote_id):
    quote = get_object_or_404(Quote, id=quote_id)
    coverage = quote.coverage.first()
    rating = quote.rating.first()
    form = quote.form.first()

    # use same names as QuoteStart to match html page
    context = {
        'new_quote': quote,
        'new_coverage': coverage,
        'new_rating': rating,
        'new_form': form,
    }

    return render(request, 'quotes/start.html', context)

# appears in footer of page during quoting process
def QuoteSave(request, quote_id):
    if request.method == 'POST':
        # Fetch the existing Quote object
        quote = Quote.objects.get(id=quote_id)
        coverage = quote.coverage.first()

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
                    elif form_type == 'coverage':
                        # Process coverage form data
                        coverage_data = {k: v for k, v in request.POST.items() if k != 'form_type'}
                        coverage_form = CoverageDetailForm(coverage_data, instance=coverage)
                        if coverage_form.is_valid():
                            coverage_form.save()
        # ... continue for other forms

        message = "Data saved successfully"
        return render(request, 'partials/_quote_save_status.html', {'message': message})

    # Handle non-POST requests here

# QuoteStart helper, value to use for number field
def generate_quote_number(quote_obj):
    quote_number = ('Q'
                    + str(quote_obj.start_date.year)
                    + str(quote_obj.start_date.month).zfill(2)
                    + '-'
                    + str(quote_obj.id).zfill(4))

    return quote_number


#@htmx_required
#@require_GET
# when Basic Details section is expanded, render the html partial within the page
#def QuoteViewBasic(request, quote_id):
#    quote = Quote.objects.get(id=quote_id)
#    return render(request, 'quotes/basic.html', {'quote': quote})


class BasicDetailView(UpdateView):
    model = Quote
    form_class = BasicDetailForm
    template_name = 'quotes/basic_form.html'
    success_url = reverse_lazy('home')

# when the term or effective_date changes, calculate the new 
def calculate_expiration_date(request):
    effective_date_str = request.GET.get('effective_date')
    term_months = request.GET.get('term', 0)
    try:
        effective_date = datetime.strptime(effective_date_str, "%Y-%m-%d")
        term_days = int(term_months) * 30  # Assume 30 days per month
        expiration_date = effective_date + timedelta(days=term_days)
        # Return just the input field you want to update to replace it entirely
        return render(request, 'partials/_quote_update_exp_date.html', {
            'expiration_date': expiration_date.strftime("%Y-%m-%d")
        })
    except ValueError:
        return JsonResponse({"error": "Invalid parameters"}, status=400)