from typing import List, Type, Dict, Optional

from server.models.devices import Sensor, BaseMeasurement
from server.models.regions import Region, RegionMap


class Aquarium:

    def __init__(self, width: int, height: int,
                 sensors: Dict[str, Type[Sensor]] = None,
                 temperature_regions: List[Region] = None):
        self.width = width
        self.height = height
        self.sensors = sensors
        self.temperature_map = RegionMap(width, height,
                                         defined_regions=temperature_regions,
                                         alias="TemperatureMap")
        # Build the Color Map with a Color Chart that corresponds to
        # temperatures.
        # self.color_map = RegionMap(width, height,
        #                            defined_regions=temperature_regions,
        #                            alias="ColorMap")
