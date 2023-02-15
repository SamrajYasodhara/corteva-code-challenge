from django.db.models import Avg, Sum
from myapp.models import WeatherData, WeatherStatistics

# Get the distinct years and weather stations in the weather data
years = WeatherData.objects.order_by().values_list('date__year', flat=True).distinct()
stations = WeatherData.objects.order_by().values_list('station', flat=True).distinct()

# Loop over all the year-station pairs and calculate the statistics
for year in years:
    for station in stations:
        data = WeatherData.objects.filter(date__year=year, station=station).exclude(max_temp=-9999).exclude(min_temp=-9999).exclude(precip=-9999)
        if data.exists():
            avg_max_temp = data.aggregate(avg_max_temp=Avg('max_temp'))['avg_max_temp'] / 10.0
            avg_min_temp = data.aggregate(avg_min_temp=Avg('min_temp'))['avg_min_temp'] / 10.0
            total_precip = data.aggregate(total_precip=Sum('precip'))['total_precip'] / 10.0 / 100.0
            WeatherStatistics.objects.update_or_create(
                year=year,
                station=station,
                defaults={
                    'avg_max_temp': avg_max_temp,
                    'avg_min_temp': avg_min_temp,
                    'total_precip': total_precip,
                }
            )
        else:
            WeatherStatistics.objects.update_or_create(
                year=year,
                station=station,
                defaults={
                    'avg_max_temp': None,
                    'avg_min_temp': None,
                    'total_precip': None,
                }
            )
