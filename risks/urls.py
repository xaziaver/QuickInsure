from django.urls import path
from .views import RiskCreateView, ViewRisk

urlpatterns = [
    path('add_Risk/ ', RiskCreateView.as_view(template_name='risks/risk_form.html'), name='add_risk'),
    path('view_Risk/ ', ViewRisk, name='view_risk'),
]