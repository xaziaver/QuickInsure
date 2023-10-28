from django.urls import path
from .views import ViewPolicy

urlpatterns = [
    path('view_policy/ ', ViewPolicy, name='view_policy'),
]