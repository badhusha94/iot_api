from rest_framework import serializers
from .models import SensorReading,SensorType,PowerPlant

class SensorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorType
        fields = ['id','type_name','unit_symbol','unit_name']

class PowerPlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerPlant
        fields = ['id','plant_name','plant_location']

class SensorReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorReading
        fields = ['id','power_plant','sensor_type','reading_parameter','reading_value','reading_datetime']