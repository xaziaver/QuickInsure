from django.shortcuts import render

def ViewPolicy(request):
    return render(request, 'policies/policy_details.html')
