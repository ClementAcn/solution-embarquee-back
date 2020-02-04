from django.urls import path, include
from rest_framework import routers

from .views import CaptureCO2ViewSet, SendCaptureCO2ViewSet, vizualize

router = routers.SimpleRouter()
router.register(r'co2', CaptureCO2ViewSet, basename='co2')
router.register(r'send-co2', SendCaptureCO2ViewSet, basename='co2')

urlpatterns = [
    path(r'', include(router.urls)),
    path('visualize-data/', vizualize, name='vizualize'),
]
