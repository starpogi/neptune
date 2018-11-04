class Sensor:
    pass


class Display:
    pass


class BaseMeasurement:

    def __init__(self, value: float = 0.0, **kwargs):
        self.value = value
        self.kwargs = kwargs

    def __repr__(self):
        return "%010.4f" % self.value
