# urls.py
from django.urls import path
from .views import ResultGpt

urlpatterns = [
    path('mathlib/', ResultGpt.as_view(), name='resultGpt'),
]
