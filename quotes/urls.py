from django.urls import path
from .views import QuoteStart, QuoteSave

urlpatterns = [
    path('add_quote/', QuoteStart, name='add_quote'),
    path('save_quote/', QuoteSave, name='save_quote'),
]