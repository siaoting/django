from rest_framework import serializers
from .models import SensorData

class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ('id', 'temperature', 'humidity', 'lighting', 'ph', 'date_created', 'date_modified')
        read_only_fields = ('date_created', 'date_modified')



