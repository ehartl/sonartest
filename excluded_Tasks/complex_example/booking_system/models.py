# booking_system/models.py
from user_management.models import User
from flight_management.models import Flight

class Booking:
    def __init__(self, booking_id: int, user: User, flight: Flight, seats_reserved: int):
        self.booking_id = booking_id
        self.user = user
        self.flight = flight
        self.seats_reserved = seats_reserved