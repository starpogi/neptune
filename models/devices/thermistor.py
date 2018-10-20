from . import Sensor, BaseMeasurement


class Probe(Sensor):
    pass


class Temperature(BaseMeasurement):

    def __init__(self, value: float = 0.0):
        self.value = value

    @property
    def farenheit(self) -> float:
        return self.value * 1.8 + 32

    @property
    def celsius(self) -> float:
        return self.value
