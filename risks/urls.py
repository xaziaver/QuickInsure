from django.urls import path
from .views import RiskCreateView, ViewRisk

urlpatterns = [
    path('add_Risk/ ', RiskCreateView.as_view(template_name='risks/form.html'), name='add_risk'),
    path('view_risk/', ViewRisk, name='view_risk'),
]