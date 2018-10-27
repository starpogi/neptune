class Sensor:
    pass


class Display:
    pass


class BaseMeasurement:

    def __init__(self, value: float = 0.0, **kwargs):
        self.value = value

    def __repr__(self):
        return "%s" % self.value
