from datetime import datetime
import os
import logging

from django.db import IntegrityError
from django.core.exceptions import ObjectDoesNotExist

from weatherapp.models import WeatherData

logger = logging.getLogger(__name__)

def ingest_weather_data():
    start_time = datetime.now()
    logger.info(f"Started weather data ingestion at {start_time}")

    data_directory = os.path.join(os.getcwd(), 'wx_data')
    file_count = 0
    record_count = 0

    for filename in os.listdir(data_directory):
        file_count += 1
        with open(os.path.join(data_directory, filename), 'r') as file:
            for line in file:
                record = line.strip().split('\t')
                date = record[0]
                max_temp = int(record[1])
                min_temp = int(record[2])
                precipitation = int(record[3])

                if max_temp == -9999 or min_temp == -9999 or precipitation == -9999:
                    continue

                try:
                    weather_data = WeatherData.objects.get(date=date)
                    weather_data.max_temp = max_temp
                    weather_data.min_temp = min_temp
                    weather_data.precipitation = precipitation
                    weather_data.save()
                except ObjectDoesNotExist:
                    WeatherData.objects.create(
                        date=date,
                        max_temp=max_temp,
                        min_temp=min_temp,
                        precipitation=precipitation
                    )
                except IntegrityError as e:
                    logger.error(f"Failed to ingest record for date {date}: {e}")
                else:
                    record_count += 1

    end_time = datetime.now()
    duration = end_time - start_time
    logger.info(f"Finished weather data ingestion at {end_time}")
    logger.info(f"Ingested {record_count} records from {file_count} files in {duration}")
