class Flight:
    def __init__(self, flight_number: str, origin: str, destination: str, departure_time: str, seats_available: int):
        self.flight_number = flight_number
        self.origin = origin
        self.destination = destination
        self.departure_time = departure_time
        self.seats_available = seats_available

    def get_details(self) -> dict:
        return {
            "flight_number": self.flight_number,
            "origin": self.origin,
            "destination": self.destination,
            "departure_time": self.departure_time,
            "seats_available": self.seats_available
        }

    def check_availability(self, seats: int) -> bool:
        return self.seats_available >= seats

    def reserve_seats(self, seats: int) -> None:
        if self.check_availability(seats):
            self.seats_available -= seats
        else:
            raise ValueError("Not enough seats available")