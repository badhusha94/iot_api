from django.shortcuts import render
from rest_framework import viewsets
from .models import SensorReading,SensorType,PowerPlant
from .serializers import SensorReadingSerializer, SensorTypeSerializer, PowerPlantSerializer

# Create your views here.
class SensorReadingViewSet(viewsets.ModelViewSet):
    queryset = SensorReading.objects.all()
    serializer_class = SensorReadingSerializer

class SensorTypeViewSet(viewsets.ModelViewSet):
    queryset = SensorType.objects.all()
    serializer_class = SensorTypeSerializer

class PowerPlantViewSet(viewsets.ModelViewSet):
    queryset = PowerPlant.objects.all()
    serializer_class = PowerPlantSerializer