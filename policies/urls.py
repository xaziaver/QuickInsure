from django.urls import path
from .views import ViewPolicy

urlpatterns = [
    path('policy/<int:policy_id>/', ViewPolicy, name='view_policy'),
]