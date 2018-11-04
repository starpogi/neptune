from . import RectilinearInterpolation


class Bicubic(RectilinearInterpolation):

    def compute(self, x: float = 0.0, y: float = 0.0) -> float:
        raise NotImplementedError


class Bilinear(RectilinearInterpolation):

    def compute(self, x: float = 0.0, y: float = 0.0) -> float:
        ix1 = ((self.x2 - x) / (self.x2 - self.x1)) * self.p1
        ix2 = ((x - self.x1) / (self.x2 - self.x1)) * self.p2

        x1 = ix1 + ix2

        ix3 = ((self.x4 - x) / (self.x4 - self.x3)) * self.p3
        ix4 = ((x - self.x3) / (self.x4 - self.x3)) * self.p4

        x2 = ix3 + ix4

        iy1 = ((self.y4 - y) / (self.y4 - self.y1)) * x1
        iy2 = ((y - self.y1) / (self.y4 - self.y1)) * x2

        return iy1 + iy2
