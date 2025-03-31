import json
import os

from ...game_classes.scene import Scene

from ...game_classes.game_object import GameObject



class module_serializer:

    def __init__ (self, module_path_structure: dict[str, str]):
        self.module_object_paths = module_path_structure

    def serialize_module(self, module_data, module_path: str) :
        module_name = module_data['name']

        if os.path.isdir(f"{module_path}/{module_name}"):
            pass
        else:
            os.makedirs(f"{module_path}/{module_name}")
            for class_types in self.module_object_paths:
                if os.path.isdir(f"{module_path}/{module_name}/{class_types}"):
                    pass
                else:
                    os.makedirs(f"{module_path}/{module_name}/{class_types}")
        with open(f"{module_path}/{module_name}/{module_name}.module", "w") as file:
            json.dump(module_data, file, indent=4)

    def serialize_object(self, object_path: str, serializable_object: GameObject):
        file_name = serializable_object.name
        serialized_data = serializable_object.serialize()

        with open(f"{object_path}/{file_name}.module", "w") as file:
            json.dump(serialized_data, file, indent=4)

    def serialize_scene(self, object_path: str, serializable_object: Scene):
        file_name = serializable_object.name
        serialized_data = serializable_object.serialize()

        with open(f"{object_path}/{file_name}.scene", "w") as file:
            json.dump(serialized_data, file, indent=4)