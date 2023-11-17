from django.shortcuts import render
from django.views.decorators.http import require_GET

from common.decorators import htmx_required
from .models import CoverageGroup

@htmx_required
@require_GET
# from quote_start.html
def ViewCoverage(request, object_id):
    object_coverage_group = CoverageGroup.objects.filter(object_id=object_id)
    return render(request, 'coverages/coverage_details.html', {'coverageGroup': object_coverage_group})