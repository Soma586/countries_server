from django.urls import path
from .views import get_region_data, get_name_data

urlpatterns = [
    path('<str:region>/', get_region_data),
    path('country/<str:name>/', get_name_data),
]