from .... import utils


class World:

    size = {str, int}

    locations: {int, int}

    def __init__(self, height: int, width: int):
        self.size = {"x": height, "y": width}