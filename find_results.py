from django.db.models import F, Sum

def calculate_and_store_statistics():
    for weather_station in WeatherData.objects.values('weather_station').distinct():
        station = weather_station['weather_station']
        for year in WeatherData.objects.filter(weather_station=station).values('year').distinct():
            y = year['year']
            weather_data = WeatherData.objects.filter(weather_station=station, year=y).exclude(max_temp=-9999, min_temp=-9999, precipitation=-9999)
            if weather_data:
                avg_max_temp = weather_data.aggregate(Avg('max_temp'))['max_temp__avg']
                avg_min_temp = weather_data.aggregate(Avg('min_temp'))['min_temp__avg']
                total_precipitation = weather_data.aggregate(Sum('precipitation'))['precipitation__sum']
                WeatherStatistics.objects.update_or_create(
                    weather_station=station,
                    year=y,
                    defaults={
                        'avg_max_temp': avg_max_temp,
                        'avg_min_temp': avg_min_temp,
                        'total_precipitation': total_precipitation
                    }
                )
