from django.urls import path, include
from rest_framework import routers

from .views import CaptureCO2ViewSet

router = routers.SimpleRouter()
router.register(r'co2', CaptureCO2ViewSet, basename='co2')

urlpatterns = [
    path(r'', include(router.urls)),
]
