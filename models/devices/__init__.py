
class Sensor:
    pass


class BaseMeasurement:

    def __init__(self, value: float = 0.0, **kwargs):
        self.value = value
