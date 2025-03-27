import json
import os

from ..utils.game_classes.item import Item
from ..utils.game_classes.world_functions.cell import Cell

class module_serializer:

    module_object_paths = {str, str}

    def __init__ (self, module_path_structure: {str, str}):
        self.module_object_paths = module_path_structure

    def serialize_item(self, item: Item, path: str):
        item_holder = item.serialize()

        # write to new file
        with open(f'{path}/{self.module_object_paths["items"]}/{item_holder["name"]}.item', "w") as file:
            json.dump(item_holder, file, indent=4)

    def serialize_cells(self, cell: Cell, path: str):
        cell_holder = {}
        cell_holder["name"] = cell.name
        cell_holder['move_cost'] = cell.move_cost

        # write to new file
        cell_path = self.module_object_paths["cells"]
        new_cell_name = cell_holder["name"]
        with open(f"{cell_path}/{path}/{new_cell_name}.cell", "W") as file:
            json.dump(cell_holder, file, indent=4)

    def serialize_module(self, module_name: str, module_path: str) :
        new_paths = {"name": module_name}
        new_paths.update(self.module_object_paths)

        os.makedirs(f"{module_path}/{module_name}")
        for class_types in self.module_object_paths:
            os.makedirs(f"{module_path}/{module_name}/{class_types}")
        with open(f"{module_path}/{module_name}/{module_name}.module", "w") as file:
            json.dump(new_paths, file, indent=4)