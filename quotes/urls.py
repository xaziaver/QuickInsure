from django.urls import path
from .views import QuoteStart, QuoteSave, QuoteResume, BasicDetailView, calculate_expiration_date

urlpatterns = [
    path('add_quote/', QuoteStart, name='add_quote'),
    path('save_quote/<int:quote_id>/', QuoteSave, name='save_quote'),
    path('resume_quote/<int:quote_id>/', QuoteResume, name='resume_quote'),
    path('view_basic/<int:pk>/', BasicDetailView.as_view(), name='view_basic'),
    path('update_exp_date/', calculate_expiration_date, name='update_exp_date'),
]