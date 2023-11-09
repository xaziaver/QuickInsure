from django.shortcuts import render
from .models import Policy
from django.views.decorators.http import require_GET

from common.decorators import htmx_required


@htmx_required
@require_GET
# from quote_start.html
def ViewPolicy(request, policy_id):
    policy = Policy.objects.get(id=policy_id)
    return render(request, 'policies/policy_details.html', {'policy': policy})