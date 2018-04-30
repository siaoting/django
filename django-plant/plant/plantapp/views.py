from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from datetime import datetime

import api
from api.models import SensorData

# Create your views here.
def index(request):
    template = loader.get_template('plantapp/index.html')
    try:
        data = SensorData.objects.latest('id')
        temp = data.temperature
        humidity = data.humidity
        lighting = data.lighting
        ph = data.ph
    except SensorData.DoesNotExist:
        temp, humidity, lighting, ph = 0, 0, 0, 0

    context = {'ph_level': str(ph),
               'humidity': str(humidity),
               'temperature' : str(temp),
               'lighting': str (lighting)
              }
    return HttpResponse(template.render(context, request))

def history(request):
    template = loader.get_template('plantapp/history.html')
    last = SensorData.objects.all().order_by('-date_created')[:50]
    phs = []
    phs.append(["Date", "PH level"])
    humids = []
    humids.append(["Date", "Humidity"])
    temperatures = []
    temperatures.append(["Date", "Temperature"])
    lights = []
    lights.append(["Date", "Lighting"])
    for v in last:
        date = v.date_created.strftime("%H:%M")
        phs.append([date, float(v.ph)])
        humids.append([date, float(v.humidity)])
        temperatures.append([date, float(v.temperature)])
        lights.append([date, float(v.lighting)])
    print(humids)
    context = {'humids': humids, 'phs': phs, 'temperatures': temperatures, 'lights': lights}
    return HttpResponse(template.render(context, request))

def status(request):
    template = loader.get_template('plantapp/status.html')
    status = "OFF"
    try:
        data = SensorData.objects.latest('id')
        print(data.date_created, datetime.now())
        last = data.date_created.timestamp()
        now = datetime.now().timestamp()
        diff = now - last
        print(diff)
        if diff < (5 * 60):
            status = "ON"
        elif diff < (10 * 60):
            status = "WARNING"
    except SensorData.DoesNotExist:
        status = "OFF"

    context = {'status': status}
    return HttpResponse(template.render(context, request))

def control(request):
    template = loader.get_template('plantapp/control.html')
    try:
        data = SensorData.objects.latest('id')
        temp = data.temperature #Todo: set to water pressure
        humidity = data.humidity
        lighting = data.lighting
        ph = data.ph
    except SensorData.DoesNotExist:
        temp, humidity, lighting, ph = 0, 0, 0, 0
        
    context = {'ph_level': str(ph),
               'humidity': str(humidity),
               'temperature' : str(temp),
               'lighting': str (lighting)
              }
 
    return HttpResponse(template.render(context, request))
