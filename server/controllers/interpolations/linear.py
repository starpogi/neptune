from . import LinearInterpolation


class Linear(LinearInterpolation):
    """
    For n=1 polynomial
    """

    def compute(self, x: float = 0.0) -> float:
        factor = ((self.y2 - self.y1) * (x - self.x1)) / (self.x2 - self.x1)
        out = self.y1 + factor
        return out
