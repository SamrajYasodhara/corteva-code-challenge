from django.urls import path
from .views import WeatherDataList, WeatherDataStatsList

urlpatterns = [
    path('weather/', WeatherDataList.as_view(), name='weather-list'),
    path('weather/stats/', WeatherDataStatsList.as_view(), name='weather-stats-list'),
]
