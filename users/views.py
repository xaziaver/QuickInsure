from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from risks.models import Risk
from quotes.models import Quote

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def home(request):
    user_risks = Risk.objects.filter(user_id=request.user.id)
    user_quotes = Quote.objects.filter(user_id=request.user.id)
    return render(request, 'users/home.html', {'risks': user_risks, 'quotes': user_quotes})