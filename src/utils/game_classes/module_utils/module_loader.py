import json
import os

from ...game_classes import item
from ...game_classes import scene
from ...game_classes import game_object
from ...game_classes.game_object import GameObject

from ..module_utils import module

from os import listdir
from os import walk



# JSON format strings for the module itself.
MODULE_NAME = "name"
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
        temp_file_list.append(filenames)
    return temp_file_list

def LoadModule(folder_path, module_name = ""):
    """Loads a module from it's folder"""
    loaded_module: module.Module
    with open(f"{folder_path}/{module_name}", 'r') as meta_file:
        data = json.load(meta_file)
        loaded_module = module.deserialize(data)
        if loaded_module is not str:
            item_file_list = GetFiles(f'{folder_path}/{loaded_module.name}/{MODULE_TYPES[0]}')
            scene_file_list = GetFiles(f'{folder_path}/{loaded_module.name}/{MODULE_TYPES[1]}')
            # load items
            for current_item in item_file_list[0]:
                with open(f'{folder_path}/{loaded_module.name}/{MODULE_TYPES[0]}/{current_item}', 'r') as item_file:
                    item_data = json.load(item_file)
                    new_object = item.deserialize(item_data)
                    if new_object is not str:
                        loaded_module.module_objects[new_object.name] = new_object
                    else:
                        print(f'ERROR loading items!\n Path is {folder_path}/{loaded_module.name}/{MODULE_TYPES[0]}/{current_item}\n Loaded data is {scene_data}')
            
            for current_scene in scene_file_list[0]:
                with open(f'{folder_path}/{loaded_module.name}/{MODULE_TYPES[1]}/{current_scene}', 'r') as scene_file:
                    scene_data = json.load(scene_file)
                    new_scene = scene.deserialize(scene_data)
                    print(new_scene.name)
                    if new_scene is not str:
                        loaded_module.scene_dict[new_scene.name] = new_scene
                    else:
                        print(f'ERROR loading scenes!\n Path is {folder_path}/{loaded_module.name}/{MODULE_TYPES[1]}/{current_scene}\n Loaded data is {scene_data}')
        else:
            print(f'ERROR LOADING {module_name} from {folder_path}')
                
    return loaded_module
        
def LoadModulesInDirectory(folder_path):
    loaded_modules = []
    loaded_module_names: list[str] = []
    module_paths = os.listdir(folder_path)
    print(module_paths)
    for path in module_paths:
        loaded_modules.append(LoadModule(folder_path, f'{path}/{path}.module'))
    
    return loaded_modules
