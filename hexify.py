from typing import Type, Dict
from models.devices import thermistor, phmeter, Sensor


class AquariumRegion:

    def __init__(self, temperature: float, x: int = 0, y: int = 0):
        self.temperature = thermistor.Temperature(value=temperature)
        self.x = x
        self.y = y


class Aquarium:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.sensors: Dict[str, Type[Sensor]] = {}

    def add_sensor(self, id: str, sensor: Sensor):
        pass


# def linear_interpolate(from_hex, to_hex, ticks=0):
#     assert len(from_hex) == 7
#     assert from_hex[0] == "#"
#     from_rgb = AquariumRegion(
#         r=int(from_hex[1:3], base=16),
#         g=int(from_hex[3:5], base=16),
#         b=int(from_hex[5:7], base=16)
#     )
#
#     assert len(to_hex) == 7
#     assert to_hex[0] == "#"
#     to_rgb = AquariumRegion(
#         r=int(to_hex[1:3], base=16),
#         g=int(to_hex[3:5], base=16),
#         b=int(to_hex[5:7], base=16)
#     )
#
#     gradient_map = [from_rgb]
#     m = ticks + 1
#
#     for i in range(ticks):
#         j = i + 1
#
#         gradient_map.append(
#             AquariumRegion(
#                 r=int(from_rgb.r + (j / m) * (to_rgb.r - from_rgb.r)),
#                 g=int(from_rgb.g + (j / m) * (to_rgb.g - from_rgb.g)),
#                 b=int(from_rgb.b + (j / m) * (to_rgb.b - from_rgb.b))
#             )
#         )
#
#     gradient_map.append(to_rgb)
#
#     return gradient_map
#
#
# l = linear_interpolate("#ffcc00", "#ffffff", ticks=29)
# print([j.hex_color_code for j in l])
