from models.devices import thermistor, phmeter, Sensor, BaseMeasurement
from models.systems import Aquarium
from models.regions import Region


regions = [
    Region(0, 0, thermistor.Temperature(0.0)),
    Region(9, 9, thermistor.Temperature(1.0)),
]
chevy = Aquarium(10, 10, temperature_regions=regions)
# print(chevy.temperature_map.regions)
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
