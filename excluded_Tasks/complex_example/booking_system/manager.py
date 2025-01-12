# booking_system/manager.py
from typing import List, Optional
from booking_system.models import Booking
from user_management.models import User
from flight_management.models import Flight

class BookingManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(BookingManager, cls).__new__(cls)
            cls._instance.bookings = []
            cls._instance.next_id = 1
        return cls._instance

    def create_booking(self, user: User, flight: Flight, seats: int) -> Booking:
        if not flight.check_availability(seats):
            raise ValueError("Not enough seats available")
        flight.reserve_seats(seats)
        booking = Booking(self.next_id, user, flight, seats)
        self.bookings.append(booking)
        self.next_id += 1
        return booking

    def cancel_booking(self, booking_id: int) -> None:
        booking = self.find_booking_by_id(booking_id)
        if booking:
            booking.flight.seats_available += booking.seats_reserved
            self.bookings.remove(booking)

    def find_booking_by_id(self, booking_id: int) -> Optional[Booking]:
        for booking in self.bookings:
            if booking.booking_id == booking_id:
                return booking
        return None