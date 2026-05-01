from dataclasses import dataclass,field
from contextlib import contextmanager
class FlightError(Exception):
    pass 
@dataclass
class Flight():
    code: str
    destination: str
    distance: int
    _status: str=field(default='SCHEDULED',init=False)

    def __post_init__(self):
        if self.distance<=0:
            raise FlightError(f'Flight {self.code} must have a positive distance')
    @property
    def is_long_haul(self):
        return self.distance>5000
    def __str__(self):
        return f'Flight {self.code} to {self.destination} ({self.distance}km) [{self._status}]'
    def __gt__(self, other):
        return self.distance>other.distance
class BoardingChecker:
    def __init__(self,flights,min_dist):
        self.flights=flights
        self.min_dist=min_dist
        self.flight_count=0
    def __iter__(self):
        return self
    def __next__(self):
        while self.flight_count<len(self.flights):
            flight=self.flights[self.flight_count]
            self.flight_count+=1
            flight._status= 'CONFIRMED' if flight.distance>self.min_dist else 'DELAYED'
            return flight
        raise StopIteration
def boarding_report(checker):
    confirmed=0
    delayed=0
    for  flight in checker:
        if flight._status=='CONFIRMED':
            confirmed+=1
        else:
            delayed+=1
        yield str(flight)
    yield f'Report: {confirmed} confirmed, {delayed} delayed'
@contextmanager
def gate_session(name):
    print(f'[BOARD] {name}')
    try:
        flights=[]
        yield flights
    except FlightError as g:
        print(f'!!! Error: {g}')
    finally:
        print(f'[GATE] {name} ({len(flights)} flights)')
        
with gate_session("Morning Departures") as flights:
    flights.append(Flight("AA100", "Paris", 2500))
    flights.append(Flight("BB200", "Tokyo", 5800))
    flights.append(Flight("CC300", "Dublin", 450))

    for line in boarding_report(BoardingChecker(flights, 1000)):
        print(line)

    print(flights[1] > flights[0])

print()

with gate_session("Evening Departures") as flights:
    flights.append(Flight("DD400", "London", -100))