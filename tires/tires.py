from abc import ABC


class Tires(ABC):
    def __init__(self, sensors: list):
        self.sensors = sensors

    def needs_service(self):
        pass
