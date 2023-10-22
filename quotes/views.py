from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from .models import Risk
from .forms import RiskForm

class RiskCreateView(CreateView):
    model = Risk  # model to interact with
    form_class = RiskForm  # form to use
    template_name = 'risk_form.html'  # template to render

    # where to redirect after successful form submission
    success_url = reverse_lazy('home')