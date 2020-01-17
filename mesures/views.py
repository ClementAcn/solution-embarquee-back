from rest_framework import viewsets
from rest_framework.response import Response

from .models import CaptureCO2
from .serializers import CaptureCO2Serializer


# Create your views here.
class CaptureCO2ViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = CaptureCO2.objects.all()
        serializer = CaptureCO2Serializer(queryset, many=True)
        return Response(serializer.data, status=200)

    def retrieve(self, request, pk=None):
        queryset = CaptureCO2.objects.all()
        data = get_object_or_404(queryset, pk=pk)
        serializer = CaptureCO2Serializer(data)
        return Response(serializer.data, status=200)

    def create(self, request):
        pass
