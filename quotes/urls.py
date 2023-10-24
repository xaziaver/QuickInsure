from django.urls import path
from .views import QuoteStart

urlpatterns = [
    path('add_quote/', QuoteStart, name="add_quote")
]