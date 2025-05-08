from django.db import models

class SensorData(models.Model):
    device_id = models.CharField(max_length=100)
    timestamp = models.DateTimeField()
    temperature = models.FloatField()
    humidity = models.FloatField()
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.device_id} at {self.timestamp}"