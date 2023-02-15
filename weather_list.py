from rest_framework.response import Response
from .models import WeatherStats

class WeatherStatsList(generics.ListAPIView):
    queryset = WeatherStats.objects.all()
    serializer_class = WeatherStatsSerializer

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)

        # group by year and station
        stats = {}
        for weather_stat in serializer.data:
            year = weather_stat['year']
            station = weather_stat['station']
            if year not in stats:
                stats[year] = {}
            if station not in stats[year]:
                stats[year][station] = {
                    'avg_max_temp': None,
                    'avg_min_temp': None,
                    'total_precipitation': None
                }
            stats[year][station]['avg_max_temp'] = weather_stat['avg_max_temp']
            stats[year][station]['avg_min_temp'] = weather_stat['avg_min_temp']
            stats[year][station]['total_precipitation'] = weather_stat['total_precipitation']

        # convert stats dict to list of objects
        data = []
        for year, year_stats in stats.items():
            for station, station_stats in year_stats.items():
                obj = {
                    'year': year,
                    'station': station,
                    'avg_max_temp': station_stats['avg_max_temp'],
                    'avg_min_temp': station_stats['avg_min_temp'],
