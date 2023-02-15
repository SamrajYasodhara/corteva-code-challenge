from rest_framework import generics
from .models import WeatherData, WeatherDataStats
from .serializers import WeatherDataSerializer, WeatherDataStatsSerializer

class WeatherDataList(generics.ListAPIView):
    queryset = WeatherData.objects.all()
    serializer_class = WeatherDataSerializer

class WeatherDataStatsList(generics.ListAPIView):
    queryset = WeatherDataStats.objects.all()
    serializer_class = WeatherDataStatsSerializer
