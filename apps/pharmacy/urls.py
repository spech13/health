from django.urls import path
from apps.pharmacy.views import diseases

urlpatterns = [
    path("diseases", diseases)
]