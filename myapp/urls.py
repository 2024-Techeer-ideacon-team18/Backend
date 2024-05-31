# urls.py
from django.urls import path
from .views import MathlibList

urlpatterns = [
    path('mathlib/', MathlibList.as_view(), name='mathlib-list'),
# path('combined/', CombinedList.as_view(), name='combined-list'),
#    path('check-mathlib/', CheckMathlib.as_view(), name='check-mathlib'),
]