from src import scene_branch

STATE_ENUMS = ["Startup",
            "New Game Menu",
            "Option Menu",
            "Exit"]



PROGRAM_NAME = "RPGEngine"
CREATOR_NAME = "Sarah A"

SELECTION_DEBUG = [
    "VALID ENTRY",
    "INVALID ENTRY",
]

CLASS_TYPES = {
    "Scene": scene_branch.Scene
}

MODULE_LOADER_PATH = "./modules"

engine_state: str

LINE_SEPERATOR_SMALL = "----------"
LINE_SEPERATOR_LARGE = "------------------------------"

def init() :
    engine_state = STATE_ENUMS[0]