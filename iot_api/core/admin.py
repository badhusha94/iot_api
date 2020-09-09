from django.contrib import admin
from .models import SensorType, PowerPlant, SensorReading

# Register your models here.
admin.site.register(SensorType)
admin.site.register(PowerPlant)
admin.site.register(SensorReading)
