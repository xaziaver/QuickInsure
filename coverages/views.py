from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import UpdateView
from django.views.decorators.http import require_GET

from common.decorators import htmx_required
from .models import CoverageGroup
from .forms import CoverageDetailForm

@htmx_required
@require_GET
# from quote_start.html
def ViewCoverage(request, object_id):
    object_coverage_group = CoverageGroup.objects.filter(object_id=object_id)
    return render(request, 'coverages/coverage_details.html', {'coverageGroup': object_coverage_group})

class CoverageDetailView(UpdateView):
    model = CoverageGroup
    form_class = CoverageDetailForm
    template_name = 'coverages/coverage_form.html'
    success_url = reverse_lazy('home')