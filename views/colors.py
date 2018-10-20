class Color:

    def __init__(self, red: float = 0.0, green: float = 0.0,
                 blue: float = 0.0):
        self.red = red
        self.green = green
        self.blue = blue

    def from_hex_color_code(self, value: str):
        if len(value) != 7:
            raise ValueError("Hex color code must be 7 characters long.")

        if value[0] != "#":
            raise ValueError("Hex color code must start with #.")

        self.red = int(value[1:3], base=16)
        self.green = int(value[3:5], base=16)
        self.blue = int(value[5:7], base=16)

    @property
    def hex_color_code(self) -> str:
        return "#%s%s%s" % (format(self.red, '02x'),
                            format(self.green, '02x'),
                            format(self.blue, '02x'))
