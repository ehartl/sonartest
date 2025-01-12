# main.py
from user_management.models import User
from user_management.repository import UserRepository
from flight_management.factory import FlightFactory
from booking_system.manager import BookingManager

def main():
    user_repo = UserRepository()
    booking_manager = BookingManager()

    # Register and login user
    user = User("john_doe", "john@example.com", "securepassword")
    user_repo.add_user(user)
    logged_in_user = user_repo.find_user_by_username("john_doe")
    if not logged_in_user or not logged_in_user.check_password("securepassword"):
        print("Login failed")
        return

    # Load flights
    flights = FlightFactory.load_flights('data/flights.json')

    # Book a flight
    flight = flights[0]
    try:
        booking = booking_manager.create_booking(logged_in_user, flight, 2)
        print(f"Booking successful: {booking.booking_id}")
    except ValueError as e:
        print(e)

    # Cancel a booking
    booking_manager.cancel_booking(booking.booking_id)
    print(f"Booking {booking.booking_id} cancelled")

if __name__ == "__main__":
    main()