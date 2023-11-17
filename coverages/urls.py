from django.urls import path
from .views import CoverageDetailView

urlpatterns = [
    path('view_coverage/<int:pk>/', CoverageDetailView.as_view(), name='view_coverage'),
]