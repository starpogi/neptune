from typing import List, Type, Dict, Optional, Union

from server.models.devices import Sensor, BaseMeasurement
from server.controllers.interpolations import RectilinearInterpolation
from server.controllers.interpolations import rectilinear


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
        return "<Region (%s, %s): %10s>" % (
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

    def interpolate(self, method: Type[RectilinearInterpolation] = None):
        """
        Perform interpolation on the matrix using the `defined_regions` as
        reference points for a rectilinear interpolation. To add a reference
        point, a new `Region` has to be appended to the `defined_regions`,
        and then `.interpolate` invoked to recaculate the matrix with the new
        reference points.
        """
        method = method or rectilinear.Bilinear
        # TODO: Dynamic sensor placement
        # TODO: What to do if there are more sensors and how to build
        # interpolation around it.
        p1 = self.matrix[0][0].value.value
        p2 = self.matrix[0][self.width - 1].value.value
        p3 = self.matrix[self.length - 1][0].value.value
        p4 = self.matrix[self.length - 1][self.width - 1].value.value

        interpolate = method(x1=0, y1=0,
                             x2=self.width - 1, y2=0,
                             x3=0, y3=self.length - 1,
                             x4=self.width - 1, y4=self.length - 1,
                             p1=p1, p2=p2, p3=p3, p4=p4)

        for y in range(self.length):
            for x in range(self.width):
                self.matrix[y][x].value.value = interpolate.compute(x, y)

    def _build_matrix(self, defined_regions) -> List[List[Region]]:
        """
        Builds a `width` x `length` matrix with `default_value` for every
        element. A list of `defined_regions` with coordinates are plugged
        into the matrix.
        """
        defined_regions = defined_regions or []
        measurement_type = BaseMeasurement
        kwargs: dict = {}

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
