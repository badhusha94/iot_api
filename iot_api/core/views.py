from rest_framework import viewsets,views,response,status
from .models import SensorReading,SensorType,PowerPlant
from .serializers import SensorReadingSerializer, SensorTypeSerializer, PowerPlantSerializer
from datetime import datetime

class SensorReadingList(views.APIView):
    queryset = SensorReading.objects
    def get(self, request, format=None):
        queryset = SensorReading.objects

        from_datetime_str = self.request.query_params.get('from',None)
        to_datetime_str = self.request.query_params.get('to',None)
        from_datetime = None
        to_datetime = None

        if from_datetime_str:
            from_datetime = datetime.strptime(from_datetime_str,'%y%m%d%H%M%S')
        if to_datetime_str:
            to_datetime = datetime.strptime(to_datetime_str,'%y%m%d%H%M%S')

        if from_datetime and to_datetime:
            queryset = queryset.filter(reading_datetime__gte=from_datetime,reading_datetime__lte=to_datetime)
        elif from_datetime and not to_datetime:
            queryset = queryset.filter(reading_datetime__gte=from_datetime)
        elif not from_datetime and to_datetime:
            queryset = queryset.filter(reading_datetime__lte=to_datetime)
        else:
            queryset = queryset.all()
        serializer = SensorReadingSerializer(queryset,many=True)
        return response.Response(serializer.data)
    
    def post(self, request, format=None):
        request.data['reading_datetime'] = datetime.strptime(str(request.data['reading_datetime']),'%y%m%d%H%M%S')
        serializer = SensorReadingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return response.Response(serializer.data, status=status.HTTP_201_CREATED)
        return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SensorTypeViewSet(viewsets.ModelViewSet):
    serializer_class = SensorTypeSerializer
    queryset = SensorType.objects.all()

class PowerPlantViewSet(viewsets.ModelViewSet):
    serializer_class = PowerPlantSerializer
    queryset = PowerPlant.objects.all()