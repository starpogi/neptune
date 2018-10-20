from . import Sensor, BaseMeasurement


class Probe(Sensor):
    pass


class Temperature(BaseMeasurement):

    def __init__(self, value: float = 0.0, **kwargs):
        super(Temperature, self).__init__(value, **kwargs)
        self.unit: str = kwargs.get('unit', 'C')
        self.value = self.celsius

        if self.unit == 'F':
            self.value = self.farenheit

    @property
    def farenheit(self) -> float:
        return self.value * 1.8 + 32

    @property
    def celsius(self) -> float:
        return self.value

    def __repr__(self):
        return "%s %s" % (self.value, self.unit)
