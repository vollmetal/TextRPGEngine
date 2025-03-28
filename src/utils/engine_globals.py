from .. import utils

STATE_ENUMS = ("Startup",
            "New Game Menu",
            "Create World",
            "Exit")



PROGRAM_NAME = "RPGEngine"
CREATOR_NAME = "Sarah A"

SELECTION_DEBUG = (
    "VALID ENTRY",
    "INVALID ENTRY",
    )


CLASS_TYPES = {
    'GameObject': ''
}

MODULE_LOADER_PATH = "./modules"

MODULE_STRUCTURE_PATH = {
    "items": "/items",
    "worlds": "/Worlds",
    "entities": "/Entities",
    "crafting_recipes": "/Crafting Recipes"
}

engine_state: str

LINE_SEPERATOR_SMALL = "----------"
LINE_SEPERATOR_LARGE = "------------------------------"

def init() :
    engine_state = STATE_ENUMS[0]