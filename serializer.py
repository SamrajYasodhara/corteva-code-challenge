from rest_framework import serializers
from .models import WeatherData, WeatherDataStats

class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = '__all__'

class WeatherDataStatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherDataStats
        fields = '__all__'
