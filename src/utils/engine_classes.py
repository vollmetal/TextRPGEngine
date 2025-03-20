

class Vector2D:

    """class handling all 2D positions and math"""

    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return (f"""Vector2D: x: {self.x},
          y: {self.y}""")


class Vector3D:

    """class handling all 3D positions and math"""

    x: int
    y: int
    z: int

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return (f"""Vector3D: x: {self.x},
                y: {self.y}, 
                z: {self.z}""")