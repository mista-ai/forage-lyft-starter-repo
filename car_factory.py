from datetime import date
from car import Car
from engine import CapuletEngine, SternmanEngine, WilloughbyEngine
from battery import SpindlerBattery, NubbinBattery


class CarFactory:
    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int,
                        last_service_mileage: int) -> Car:
        battery = SpindlerBattery(current_date, last_service_date)
        engine = CapuletEngine(last_service_mileage, current_mileage)
        return Car(engine, battery)

    @staticmethod
    def create_glissade(current_date: date, last_service_date: date, current_mileage: int,
                        last_service_mileage: int) -> Car:
        battery = SpindlerBattery(current_date, last_service_date)
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        return Car(engine, battery)

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool) -> Car:
        battery = SpindlerBattery(current_date, last_service_date)
        engine = SternmanEngine(warning_light_on)
        return Car(engine, battery)

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int,
                         last_service_mileage: int) -> Car:
        battery = NubbinBattery(current_date, last_service_date)
        engine = WilloughbyEngine(last_service_mileage, current_mileage)
        return Car(engine, battery)

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int,
                      last_service_mileage: int) -> Car:
        battery = NubbinBattery(current_date, last_service_date)
        engine = CapuletEngine(last_service_mileage, current_mileage)
        return Car(engine, battery)
