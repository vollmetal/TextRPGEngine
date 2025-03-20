from ...engine_classes import Vector3D
from .cell import Cell


class Worldspace:

    name: str

    size = dict[str, int]

    cells: dict[Vector3D, Cell]

    def __init__(self, name: str, length: int = 1, width: int = 1, height: int = 1, cells: dict[Vector3D, Cell] = {}):
        self.name = name
        self.size = {"x": length, "y": width, "z": height}
        self.cells = cells

    
