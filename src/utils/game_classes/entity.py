

class Entity:
    
    name: str

    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"This is {self.name}"
    
    def __repr__(self):
        return f"DEBUG: {self.name}"