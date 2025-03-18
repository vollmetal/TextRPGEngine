import json
from ... import utils
from ...utils import engine_globals, game_classes
from ...module_utils import module

from os import listdir
from os import walk

# JSON format strings for the module itself.
MODULE_NAME = "moduleName"
MODULE_SCENE_OBJECT = "scenes"

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

def LoadFile(file_path, file) :
    """
    Creates and returns a new game module from selected JSON file.

    file_path = path to the requested file
    file = name of the requested file
    """
    new_module: module.Module
    with open(file_path + '/' + file, 'r') as selected_file:
        data = json.load(selected_file)
        new_module = module.Module(data[MODULE_NAME])
        for module_scene in data[MODULE_SCENE_OBJECT].values() :
            new_scene = utils.game_classes.world_functions.scene_branch.Scene(module_scene[SCENE_NAME], module_scene[SCENE_DESCRIPTION])
            new_scene.add_user_input(module_scene[SCENE_USER_INPUTS])
            if module_scene["start_scene"]:
                new_module.add_scenes(new_scene.name, new_scene, True)
            else:
                new_module.add_scenes(new_scene.name, new_scene, False)
    return new_module