from typing import List, Type, Dict, Optional
from models.devices import Sensor, BaseMeasurement
from controllers.interpolations import rectilinear


class Region:

    def __init__(self, x: int = 0, y: int = 0,
                 value: Type[BaseMeasurement] = None):
        self.value = value
        self.x = x
        self.y = y

    def __repr__(self):
        return "<Region (%s, %s): %s>" % (
            self.x,
            self.y,
            self.value
    )


class RegionMap:

    def __init__(self, width: int, height: int,
                 alias: str = None,
                 defined_regions: List[Region] = None,
                 interpolation: Type[rectilinear.Base] = rectilinear.Bilinear):
        self.width = width
        self.height = height
        self.alias = alias or "RegionMap"
        self.interpolation = interpolation
        self.regions = [[Region()] * width] * height
        self._build_region_map(defined_regions)

    def _build_region_map(self, defined_regions):
        """
        Builds the rest of the regions even with partial sectors. Sets the
        region map with a complete map, taking into account gaps.
        """
        defined_regions = defined_regions or []
        # measurement_type = BaseMeasurement

        for defined_region in defined_regions:
            x = defined_region.x
            y = defined_region.y
            self.regions[y][x] = defined_region
            # measurement_type = defined_region.value.__class__

        # Normalize all regions with the correct coordinates
        for i in range(self.height):
            for j in range(self.width):
                print(i, j)
                self.regions[i][j].x = j
                self.regions[i][j].y = i

    def __repr__(self):
        return "<%s (%s x %s)>" % (
            self.alias,
            self.width,
            self.height
    )
