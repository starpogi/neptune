from server.models.devices import thermistor, phmeter, Sensor, BaseMeasurement
from server.models.systems import Aquarium
from server.models.regions import Region

from server.controllers.interpolations import rectilinear

import pprint

pp = pprint.PrettyPrinter(width=150, compact=True)

regions = [
    Region(0, 0, thermistor.Temperature(4.0)),
    Region(4, 0, thermistor.Temperature(0.0)),
    Region(0, 4, thermistor.Temperature(0.0)),
    Region(4, 4, thermistor.Temperature(0.0))
]
tank = Aquarium(5, 5, temperature_regions=regions)
tank.temperature_map.interpolate()
pp.pprint(tank.temperature_map.matrix)
