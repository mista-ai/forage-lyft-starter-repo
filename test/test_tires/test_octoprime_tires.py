import unittest
from tires.octoprime_tires import OctoprimeTires


class TestOctoprimeTires(unittest.TestCase):
    def test_needs_service_true(self):
        sensors = [0.9, 0.9, 0.9, 0.3]
        tires = OctoprimeTires(sensors)
        self.assertTrue(tires.needs_service())

    def test_needs_service_false(self):
        sensors = [0.9, 0.9, 0.9, 0.2]
        tires = OctoprimeTires(sensors)
        self.assertFalse(tires.needs_service())