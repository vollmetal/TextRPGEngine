from ..utils import engine_globals

class Module:

    def __init__ (self, name: str) :
        self.name = name
        self.module_objects = {}

    def __str__(self):
        return f"Module name: {self.name}\n"


    def run (self) :
        pass