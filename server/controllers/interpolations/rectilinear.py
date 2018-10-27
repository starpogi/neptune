from . import RectilinearInterpolation


class Bicubic(RectilinearInterpolation):
    pass


class Bilinear(RectilinearInterpolation):

    def compute(self, x: float = 0.0, y: float = 0.0) -> float:
        return 0.0
