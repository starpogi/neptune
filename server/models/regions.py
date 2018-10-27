from typing import List, Type, Dict, Optional, Union

from server.models.devices import Sensor, BaseMeasurement
from server.controllers.interpolations import RectilinearInterpolation


class Region:
    """
    A Region represents an element in a `RegionMap` or matrix.
    """

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
    """
    A Region Map is a matrix of `width` x `length` dimensions that consists
    of `Regions`. Each `Region` represents a value and coordinate that is used
    to calculate a desired rectilinear interpolation. Typically, for a
    rectilinear interpolation to work, at least 4 `defined_regions` have to
    be provided so that the interpolation will sufficient reference points.
    """

    def __init__(self, width: int, length: int,
                 alias: str = "RegionMap",
                 defined_regions: List[Region] = None,
                 default_value: float = 0.0):
        self.width = width
        self.length = length
        self.alias = alias
        self.default_value = default_value
        self.matrix = self._build_matrix(defined_regions)

    def interpolate(self, method: Type[RectilinearInterpolation]):
        """
        Perform interpolation on the matrix using the `defined_regions` as
        reference points for a rectilinear interpolation. To add a reference
        point, a new `Region` has to be appended to the `defined_regions`,
        and then `.interpolate` invoked to recaculate the matrix with the new
        reference points.
        """
        pass

    def _build_matrix(self, defined_regions) -> List[List[Region]]:
        """
        Builds a `width` x `length` matrix with `default_value` for every
        element. A list of `defined_regions` with coordinates are plugged
        into the matrix.
        """
        defined_regions = defined_regions or []
        measurement_type = BaseMeasurement

        # Assume that every degined region has the same Measurement Type
        if defined_regions:
            measurement_type = defined_regions[0].value.__class__

        matrix = []
        # Normalize all regions with the correct coordinates
        for i in range(self.length):
            vector = []

            for j in range(self.width):
                vector.append(Region(j, i,
                                     measurement_type(self.default_value)))

            matrix.append(vector)

        # Add the known/defined regions
        for defined_region in defined_regions:
            x = defined_region.x
            y = defined_region.y
            matrix[y][x] = defined_region

        return matrix

    def __repr__(self):
        return "<%s (%s x %s)>" % (
            self.alias,
            self.width,
            self.length
    )
