import json
import os

from ... import utils

class module_serializer:

    module_object_paths = {str, str}

    def __init__ (self, module_path_structure: {str, str}):
        self.module_object_paths = module_path_structure

    def serialize_item(self, item: utils.game_classes.item.Item, path: str):
        item_holder = {}
        item_holder["name"] = item.get_name()
        item_holder["size"] = {"x": item.get_size().x, 
                            "y": item.get_size().y, 
                            "z": item.get_size().z}
        item_holder["weight"] = item.get_weight()
        item_holder["value"] = item.get_value()
        item_holder["icon"] = item.get_icon()
        item_holder["keywords"] = item.get_keywords()
        item_holder["category"] = item.get_category()
        item_holder["crafting_recipes"] = item.get_crafting_recipes()

        # write to new file
        with open(self.module_object_paths["items"] + path + item_holder["name"] + ".json", "W") as file:
            json.dump(item_holder, file)

    def serialize_module(self, module_name: str, module_path: str) :
        
        with open(module_path + "/" + module_name + ".json", "w") as file:
            json.dump(self.module_object_paths, file, indent=4)