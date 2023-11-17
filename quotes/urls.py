from django.urls import path
from .views import QuoteStart, QuoteSave, BasicDetailView

urlpatterns = [
    path('add_quote/', QuoteStart, name='add_quote'),
    path('save_quote/', QuoteSave, name='save_quote'),
    path('view_basic/<int:quote_id>/', BasicDetailView.as_view(), name='view_basic')
]