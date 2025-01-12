# flight_management/factory.py
import json
from flight_management.models import Flight

class FlightFactory:
    @staticmethod
    def load_flights(file_path: str) -> list:
        with open(file_path, 'r') as file:
            flights_data = json.load(file)
        return [Flight(**data) for data in flights_data]