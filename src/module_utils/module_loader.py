import json

from ..utils.game_classes.world_functions.scene_branch import Scene
from ..utils.engine_classes import Vector3D
from ..utils.game_classes.item import Item

from .module import Module

from os import listdir
from os import walk

# JSON format strings for the module itself.
MODULE_NAME = "moduleName"
MODULE_TYPES = ('items',
                'scenes')

# JSON format strings for the scenes.
SCENE_NAME = "name"
SCENE_DESCRIPTION = "description"
SCENE_USER_INPUTS = "user_inputs"


def GetFiles(path) :
    """ Returns all files at the given path. """
    temp_file_list = []
    for (dirpath, dirnames, filenames) in walk(path):
        temp_file_list.extend(filenames)
    return temp_file_list

def LoadModule(folder_path, module_name = ""):
    """Loads a module from it's folder"""
    loaded_module: Module
    with open(folder_path + '/' + module_name, 'r') as meta_file:
        data = json.load(meta_file)
        loaded_module = Module(data[MODULE_NAME])
        item_file_list = GetFiles(f'{folder_path}/{module_name}/{MODULE_TYPES[0]}')
        scene_file_list = GetFiles(f'{folder_path}/{module_name}/{MODULE_TYPES[1]}')
        # load items
        for item in item_file_list:
            with open(f'{folder_path}/{module_name}/{MODULE_TYPES[0]}/{item}') as item_file:
                item_data = item_file
                size = Vector3D(item_data['size']['x'], item_data['size']['y'], item_data['size']['z'])
                new_item = Item(
                    item_data['name'],
                    size,
                    item_data['weight'],
                    item_data['value'],
                    item_data['icon'],
                    item_data['category'],
                    item_data['keywords'],
                    item_data['crafting_recipes']
                )
            loaded_module.items[new_item.name] = new_item
        # load scenes
        for scene in scene_file_list:
            with open(f'{folder_path}/{module_name}/{MODULE_TYPES[0]}/{scene}') as scene_file:
                scene_data = scene_file
                new_scene = Scene(
                    scene_data['name'],
                    scene_data['description']
                )
            loaded_module.scenes[new_scene.name] = new_scene
    return loaded_module
        
def LoadModulesInDirectory(folder_path):
    loaded_modules = []
    for (dirpath, dirnames, filenames) in walk(folder_path):
        module_folder = dirpath
        for (dirpath, dirnames, filenames) in walk(f'{folder_path}/{module_folder}'):
            for file in filenames:
                loaded_module = LoadModule(dirpath, filenames)
                loaded_modules.append(loaded_module)
    return loaded_modules