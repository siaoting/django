from django.db import models


class SensorData(models.Model):
    """This class represents the bucketlist model."""
    temperature = models.CharField(max_length=10, blank=False)
    humidity = models.CharField(max_length=10, blank=False)
    lighting = models.CharField(max_length=10, blank=False)
    ph = models.CharField(max_length=10, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "id = {}, temperature = {}, humidity = {}, lighting = {}, ph = {}". \
                format(self.id, self.temperature, self.humidity, self.lighting, self.ph)

