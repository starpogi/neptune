from typing import List, Type, Dict, Optional, Union
from models.devices import Sensor, BaseMeasurement
from controllers.interpolations import rectilinear


class Region:

    def __init__(self, x: int = 0, y: int = 0,
                 value: Union[BaseMeasurement, Type[BaseMeasurement]] = None):
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
        self.regions = self._build_region_map(defined_regions)
        print(self.regions)

    def _build_region_map(self, defined_regions) -> List[List[Region]]:
        """
        Builds the rest of the regions even with partial sectors. Sets the
        region map with a complete map, taking into account gaps.
        """
        defined_regions = defined_regions or []
        measurement_type = BaseMeasurement

        # Assume that every degined region has the same Measurement Type
        if defined_regions:
            measurement_type = defined_regions[0].value.__class__

        regions = []
        # Normalize all regions with the correct coordinates
        for i in range(self.height):
            row = []

            for j in range(self.width):
                row.append(Region(j, i, measurement_type(0.0)))

            regions.append(row)

        # Add the known/defined regions
        for defined_region in defined_regions:
            x = defined_region.x
            y = defined_region.y
            regions[y][x] = defined_region

        return regions

    def __repr__(self):
        return "<%s (%s x %s)>" % (
            self.alias,
            self.width,
            self.height
    )
