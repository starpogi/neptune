class LinearInterpolation:
    def __init__(self, x1: float = 0.0, y1: float = 0.0,
                 x2: float = 0.0, y2: float = 0.0):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def compute(self, x: float = 0.0) -> float:
        return 0.0


class RectilinearInterpolation:
    def __init__(self, x1: float = 0.0, x2: float = 0.0,
                 x3: float = 0.0, x4: float = 0.0,
                 y1: float = 0.0, y2: float = 0.0,
                 y3: float = 0.0, y4: float = 0.0,
                 p1: float = 0.0, p2: float = 0.0,
                 p3: float = 0.0, p4: float = 0.0):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.p4 = p4

        self.x1 = x1
        self.x2 = x2
        self.x3 = x3
        self.x4 = x4

        self.y1 = y1
        self.y2 = y2
        self.y3 = y3
        self.y4 = y4

    def compute(self, x: float = 0.0, y: float = 0.0) -> float:
        return 0.0
