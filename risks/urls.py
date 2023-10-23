from django.urls import path
from .views import RiskCreateView

urlpatterns = [
    path('add_Risk/ ', RiskCreateView.as_view(template_name='risks/risk_form.html'), name='add_risk'),
]