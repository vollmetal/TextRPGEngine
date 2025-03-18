

class Vector2D:

    """class handling all 2D positions and math"""

    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y


class Vector3D:

    """class handling all 3D positions and math"""

    x: int
    y: int
    z: int

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_x(self):
        return self.x
    
    def get_y(self):
        return self.y
    
    def get_z(self):
        return self.z
    
    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def set_z(self, new_z):
        self.z = new_z