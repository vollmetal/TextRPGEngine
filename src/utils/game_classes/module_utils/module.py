import json
from ....utils.game_classes.rt_thread import RealTimeThread
from ....utils.game_classes.scene import Scene
from ....utils import engine_globals

class Module:

    def __init__ (self, name: str, start_scene: str, version_number: str, author_name: str) :
        self.name = name
        self.version_number = version_number
        self.author_name = author_name
        self.module_objects = {}
        self.scene_dict = {}
        self.start_scene = start_scene
        self.module_thread = RealTimeThread(name= f'{self.name} main thread', start_scene= start_scene, module_data= self)

    def __str__(self):
        return f"Module name: {self.name}\n"

    def serialize(self) -> dict[str]:
        """serialize the object into an easily writable dictionary. DOES NOT LOAD OBJECTS WITHIN MODULE"""
        serialized_object = {}
        serialized_object['name'] = self.name
        serialized_object['version'] = self.version_number
        serialized_object['author'] = self.author_name
        serialized_object['start scene'] = self.start_scene
        serialized_object['scene path'] = '/scenes'
        return serialized_object

    def run (self) :
        self.module_thread.tick()

def deserialize(object_data) -> Module | str:
    '''Load up a module using json and return it or an error message'''
    EXCEPTION_MESSAGE = 'Error loading object data. Please check json structure!'
    loaded_object = ''
    try:
        loaded_object = Module(name= object_data['name'], version_number= object_data['version'], author_name= object_data['author'], start_scene= object_data['start scene'])
    except:
        loaded_object = EXCEPTION_MESSAGE
    return loaded_object