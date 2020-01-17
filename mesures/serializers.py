from rest_framework import serializers

class CaptureCO2Serializer(serializers.Serializer):
    date = serializers.DateTimeField()
    ppm = serializers.IntegerField()
