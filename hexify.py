from server.models.devices import thermistor, phmeter, Sensor, BaseMeasurement
from server.models.systems import Aquarium
from server.models.regions import Region


regions = [
    Region(0, 0, thermistor.Temperature(0.0)),
    Region(9, 9, thermistor.Temperature(1.0)),
]
chevy = Aquarium(10, 10, temperature_regions=regions)
print(chevy.temperature_map)
