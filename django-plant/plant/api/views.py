from django.shortcuts import render
from rest_framework import generics
from .serializers import SensorDataSerializer
from .models import SensorData

class SetSensorData(generics.ListCreateAPIView):
    serializer_class = SensorDataSerializer
    def get_queryset(self):
        return None

    def perform_create(self, serializer):
        #print("perform_create", serializer)
        serializer.save()

class GetLastSensorData(generics.RetrieveAPIView):
    serializer_class = SensorDataSerializer
    def get_object(self):
        try:
            query = SensorData.objects.latest('id')
        except SensorData.DoesNotExist:
            query = ""
        return query

class GetSensorData(generics.ListCreateAPIView):
    serializer_class = SensorDataSerializer
    def get_queryset(self):
        if 'size' not in self.request.query_params:
            queryset = SensorData.objects.all()
        else:
            size = int(self.request.query_params['size'])
            queryset = SensorData.objects.all().order_by('-id')[:size]
        return queryset



