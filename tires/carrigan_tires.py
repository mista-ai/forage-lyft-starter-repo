from tires.tires import Tires


class CarriganTires(Tires):
    def needs_service(self):
        for sensor in self.sensors:
            if sensor >= 0.9:
                return True
        return False
