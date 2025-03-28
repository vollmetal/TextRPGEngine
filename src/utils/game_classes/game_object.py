

from typing import Callable


class GameObject:
    """Base class for all game objects. DO NOT CALL BY ITSELF, INHERIT FROM INTO A NEW CLASS INSTEAD."""


    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f'Object name is: {self.name}'

    def run(self, callable_to_run: str, *args):
        pass
    
    def serialize(self) -> dict[str]:
        """serialize the object into an easily writable dictionary"""
        serialized_object = {}
        serialized_object['name'] = self.name
        return serialized_object
    
def deserialize(object_data) -> GameObject | str:
    EXCEPTION_MESSAGE = 'Error loading object data. Please check json structure!'
    loaded_object = ''
    try:
        loaded_object = GameObject(object_data['name'])
    except:
        loaded_object = EXCEPTION_MESSAGE
    return loaded_object