from .. import utils

STATE_ENUMS = ["Startup",
            "New Game Menu",
            "Create World",
            "Exit"]



PROGRAM_NAME = "RPGEngine"
CREATOR_NAME = "Sarah A"

SELECTION_DEBUG = [
    "VALID ENTRY",
    "INVALID ENTRY",
]

CLASS_TYPES = {
    "Scene": utils.game_classes.world_functions.scene_branch.Scene,
    "Item" : ""
}

MODULE_LOADER_PATH = "./modules"

MODULE_STRUCTURE_PATH = {
    "Items": "/items",
    "Worlds": "/worlds",
    "Entities": "/entities",
    "Crafting Recipes": "/crafting_recipes"
}

engine_state: str

LINE_SEPERATOR_SMALL = "----------"
LINE_SEPERATOR_LARGE = "------------------------------"

def init() :
    engine_state = STATE_ENUMS[0]