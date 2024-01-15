from tires.tires import Tires


class OctoprimeTires(Tires):
    def needs_service(self):
        if sum(self.sensors) >= 3:
            return True
        return False
