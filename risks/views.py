from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView
from django.views.decorators.http import require_GET

from common.decorators import htmx_required
from .models import Risk
from .forms import RiskForm


class RiskCreateView(CreateView):
    model = Risk
    form_class = RiskForm
    template_name = 'risk_form.html'

    # Entry point for GET, POST, etc.
    def dispatch(self, request, *args, **kwargs):
        action = request.POST.get('action')
        print(request.POST)
        if action == 'cancel':
            if request.headers.get('HX-Request'):
                return render(request, 'risks/_risk_addDelView.html', {'risks': self.model.objects.filter(user_id=request.user.id)})
            else:
                return HttpResponseRedirect(self.get_success_url())
        elif action == 'add' or action is None:
            return super().dispatch(request, *args, **kwargs)

    # Called for GET requests
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    # Called for POST requests
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)

    # Returns the form class to be used
    def get_form_class(self):
        return super().get_form_class()

    # Returns an instance of the form to be used
    def get_form(self, form_class=None):
        return super().get_form(form_class)

    # Called if the form is valid
    def form_valid(self, form):
        form.instance.user = self.request.user
        response = super().form_valid(form)
        if self.request.headers.get('HX-Request'):
            return render(self.request, 'risks/_risk_addDelView.html', {'risks': self.model.objects.filter(user_id=self.request.user.id)})
        return response

    # Called if the form is invalid
    def form_invalid(self, form):
        return super().form_invalid(form)

    # Returns the URL to redirect to when the form is successfully submitted
    def get_success_url(self):
        return reverse_lazy('home')


@htmx_required
@require_GET
# from quote_start.html
def ViewRisk(request):
    user_risks = Risk.objects.filter(user_id=request.user.id)
    return render(request, 'risks/risk_details.html', {'risks': user_risks})