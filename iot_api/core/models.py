from django.db import models
from datetime import datetime
from django.conf import settings

# Create your models here.
class SensorType(models.Model):
    type_name = models.CharField(max_length=50,blank=False,null=False,verbose_name='Type Name')
    unit_symbol = models.CharField(max_length=10,blank=False,null=False,verbose_name='Unit Symbol')
    unit_name = models.CharField(max_length=50,verbose_name='Unit Name')
    created_on = models.DateTimeField(editable=False)
    updated_on = models.DateTimeField(editable=False)
    active = models.BooleanField(default=True,null=False,verbose_name='Active')

    class Meta:
        verbose_name = 'Sensor Type'
        verbose_name_plural = 'Sensor Types'

    def __str__(self):
        return self.type_name
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_on = datetime.now()
            self.updated_on = datetime.now()
        else:
            self.updated_on = datetime.now()
        return super(SensorType,self).save(*args,**kwargs)

class PowerPlant(models.Model):
    plant_name = models.CharField(max_length=100,blank=False,null=False,verbose_name='Plant Name')
    plant_location = models.CharField(max_length=100,verbose_name='Plant Location')
    created_on = models.DateTimeField(editable=False)
    updated_on = models.DateTimeField(editable=False)
    active = models.BooleanField(default=True,null=False,verbose_name='Active')
    
    class Meta:
        verbose_name = 'Power Plant'
        verbose_name_plural = 'Power Plants'

    def __str__(self):
        return self.plant_name
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.created_on = datetime.now()
            self.updated_on = datetime.now()
        else:
            self.updated_on = datetime.now()
        return super(PowerPlant,self).save(*args,**kwargs)

class SensorReading(models.Model):
    power_plant = models.ForeignKey(
        to=PowerPlant,
        related_name='plant_readings',
        blank=True,
        null=False,
        on_delete=models.CASCADE,
        verbose_name='Power Plant'
    )
    sensor_type = models.ForeignKey(
        to=SensorType,
        related_name='sensor_readings',
        blank=True,
        null=False,
        on_delete=models.CASCADE,
        verbose_name='Sensor Type'
    )
    reading_parameter = models.CharField(max_length=100,null=False,blank=False)
    reading_value = models.FloatField(null=False,blank=False)
    reading_datetime = models.DateTimeField(null=False,blank=False)

    class Meta:
        verbose_name = 'Sensor Reading'
        verbose_name_plural = 'Sensor Readings'
        ordering = ['-reading_datetime']

    def __str__(self):
        return '{0} ({1}): {2} reading on {3} is {4} {5}'.format(
            self.power_plant.plant_name,
            self.power_plant.plant_location,
            self.sensor_type.type_name,
            self.reading_datetime.strftime('%x at %X'),
            self.reading_value,
            self.sensor_type.unit_symbol
        )
    
    def save(self,*args,**kwargs):
        if not self.power_plant_id:
            power_plant, created = PowerPlant.objects.get_or_create(
                plant_name= settings.DEFAULT_POWER_PLANT_NAME,
                plant_location= settings.DEFAULT_POWER_PLANT_LOCATION
            )
            self.power_plant_id = power_plant.id
        if not self.sensor_type_id:
            sensor_type, created = SensorType.objects.get_or_create(
                type_name = self.reading_parameter,
                unit_symbol = settings.DEFAULT_MEASUREMENT_UNIT
            )
            self.sensor_type_id = sensor_type.id
        return super(SensorReading,self).save(*args,**kwargs)
    
