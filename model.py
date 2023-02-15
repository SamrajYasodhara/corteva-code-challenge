from django.db import models

class WeatherData(models.Model):
    date = models.DateField()
    max_temp = models.FloatField()
    min_temp = models.FloatField()
    precipitation = models.FloatField()
    station = models.ForeignKey(WeatherStation, on_delete=models.CASCADE)

class WeatherStation(models.Model):
    name = models.CharField(max_length=100)
