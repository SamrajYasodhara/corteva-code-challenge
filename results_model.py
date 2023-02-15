from django.db import models

class WeatherStatistics(models.Model):
    weather_station = models.ForeignKey(WeatherData, on_delete=models.CASCADE)
    year = models.IntegerField()
    avg_max_temp = models.FloatField(null=True)
    avg_min_temp = models.FloatField(null=True)
    total_precipitation = models.FloatField(null=True)
