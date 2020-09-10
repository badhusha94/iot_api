from datetime import datetime,timedelta
import random
import json
objects = []
no = int(input('Enter no of readings to be generated : ')) + 1
secs = int(input('Enter reading interval in secs : '))
tmpstart =  int(input('Enter minimum Temperature : '))
tmpend = int(input('Enter maximum Temperature : '))
for i in range(1,no):
    time = datetime.now() + timedelta(seconds=i*secs)
    randnumber = random.randint(tmpstart,tmpend) + round(float(random.random()),2)
    dictobj = {
        "model": "core.sensorreading",
        "pk": i,
        "fields": {
           "power_plant": 1,
           "sensor_type": 1,
           "reading_value": randnumber, 
           "reading_datetime": time.strftime("%Y-%m-%dT%H:%M:%SZ"), 
           "reading_parameter": "Temperature"
          }
        }
    objects.append(dictobj)
out_file = open('SensorReadings.json','w')
json.dump(objects,out_file,indent=2)
print('Fixture file for Django iot_api app generated!')
out_file.close()
