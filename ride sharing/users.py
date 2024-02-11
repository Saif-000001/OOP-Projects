from abc import ABC, abstractmethod
from datetime import datetime

class Ride_Sharing:
    def __init__(self, company_name) -> None:
        self.company_name = company_name
        self.riders = []
        self.drivers = []
        self.rides = []
    
    def add_rider(self, rider):
        self.riders.append(rider)
    
    def add_driver(self, driver):
        self.drivers.append(driver)
    
    def __repr__(self) -> str:
        return f'{self.company_name} with riders: {len(self.riders)} and drivers: {len(self.drivers)}'

class Users(ABC):
    def __init__(self, name, email, nid) -> None:
        self.name = name
        self.email = email
        # TODO: set user id dynamically
        self.__id = 0
        self.__nid = nid
        self.__wallet = 0
    
    @abstractmethod
    def display_profile(self):
        return NotImplementedError

class Rider(Users):
    def __init__(self, name, email, nid, current_location, initial_amount) -> None:
        self.current_ride = None
        self.wallet = initial_amount
        self.current_location = current_location
        super().__init__(name, email, nid)
    
    def display_profile(self):
        print(f"Rider: with name: {self.name} and email: {self.email}")
    
    def load_cash(self, amount):
        if amount > 0:
            self.wallet += amount
    
    def update_location(self, current_location):
        self.current_location = current_location
    
    def request_ride(self, ride_sharing, destination):
        if not self.current_ride:
            print("hello")
            ride_request = Ride_Request(self,destination)
            ride_matching = Ride_Matching(ride_sharing.drivers)
            ride= ride_matching.find_driver(self, ride_request)
            self.current_ride = ride

    def show_current_ride(self) ->None:
        print(self.current_ride)

class Driver(Users):
    def __init__(self, name, email, nid, current_location) -> None:
        self.current_location = current_location
        self.wallet = 0
        super().__init__(name, email, nid)

    def display_profile(self):
        print(f"Driver with name: {self.name} and email: {self.email}")

    def accept_ride(self, ride):
        ride.set_driver(self)

class Ride:
    def __init__(self, start_location, end_location) -> None:
        self.start_location = start_location
        self.end_location = end_location
        self.driver = None
        self.rider = None
        self.start_time = None
        self.end_time = None
        self.eastimated_fare = None
    
    def set_driver(self, driver):
        self.driver = driver
    
    def start_ride(self):
        self.start_time = datetime.now()
    
    def end_ride(self):
        self.end_ride = datetime.now()
        self.rider.wallet -= self.eastimated_fare
        self.driver.wallet += self.eastimated_fare
    
    def __repr__(self) -> str:
        return f"Ride Details. Started: {self.start_location} to {self.end_location}"

class Ride_Request:
    def __init__(self, rider, end_location) -> None:
        self.rider = rider
        self.end_location = end_location
    

class Ride_Matching:
    def __init__(self, driver) -> None:
        self.available_drivers = driver
    
    def find_driver(self, ride_request):
        if len(self.available_drivers) > 0:
            driver = self.available_drivers
            ride = Ride(ride_request.ride.current_location, ride_request.end_location)
            driver.accept_ride(ride)
            return ride

class Vehicle(ABC):
    speed = {
        'car':50,
        'bike':60,
        'cng':15
    }
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        self.vehicle_type = vehicle_type
        self.license_plate = license_plate
        self.rate = rate
        self.status = 'available'
    
    @abstractmethod
    def start_drive(self):
        pass

class Car(Vehicle):
    def __init__(self, vehicle_type, license_plate, rate) -> None:
        super().__init__(vehicle_type, license_plate, rate)
    
    def start_drive(self):
        self.status = "unavailable"

niye_jao = Ride_Sharing('niye jao')
shakib = Rider('Shakib', 'shakib@khan.com', 1225, 'mohakhali', 1200)
niye_jao.add_rider(shakib)
kala_pakhi = Driver('Kala', 'kala@pakhi', 12345, 'uttora 1')
niye_jao.add_driver(kala_pakhi)
# shakib.request_ride(niye_jao,'aksdflj')
print(niye_jao)
shakib.show_current_ride()
