from django.urls import path
from .views import ViewCoverage

urlpatterns = [
    path('view_coverage/<int:object_id>/', ViewCoverage, name='view_coverage'),
]