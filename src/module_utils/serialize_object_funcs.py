import json
import os

from ..utils.game_classes.game_object import GameObject



class module_serializer:

    module_object_paths = {str, str}

    def __init__ (self, module_path_structure: {str, str}):
        self.module_object_paths = module_path_structure

    def serialize_module(self, module_name: str, module_path: str) :
        new_paths = {"name": module_name}
        new_paths.update(self.module_object_paths)

        os.makedirs(f"{module_path}/{module_name}")
        for class_types in self.module_object_paths:
            os.makedirs(f"{module_path}/{module_name}/{class_types}")
        with open(f"{module_path}/{module_name}/{module_name}.module", "w") as file:
            json.dump(new_paths, file, indent=4)

    def serialize_object(self, object_path: str, serializable_object: GameObject):
        file_name = serializable_object.name
        serialized_data = serializable_object.serialize()

        with open(f"{object_path}/{file_name}.module", "w") as file:
            json.dump(serialized_data, file, indent=4)