from . import Sensor, BaseMeasurement


class Probe(Sensor):
    pass


class Temperature(BaseMeasurement):

    def __init__(self, value: float = 0.0, unit: str = 'C'):
        super(Temperature, self).__init__(value)
        units = {
            'F': self.farenheit,
            'C': self.celsius,
            'K': self.kelvin
        }

        self.unit = units.get(unit, self.celsius)

    @property
    def farenheit(self) -> float:
        return self.value * 1.8 + 32

    @property
    def kelvin(self) -> float:
        return self.value + 273.15

    @property
    def celsius(self) -> float:
        return self.value

    def __repr__(self):
        return "%s %s" % (self.value, self.unit)
