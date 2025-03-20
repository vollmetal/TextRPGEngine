from ..utils.game_classes.item import Item
from ..utils.game_classes.world_functions.scene_branch import Scene
from ..utils import engine_globals

class Module:
    name: str

    scenes: dict[str : Scene]

    items: dict[str: Item]

    initial_scene: Scene

    current_scene: str

    def __init__ (self, name: str) :
        self.name = name
        self.scenes = {}
        self.items = {}
        self.initial_scene = Scene
        self.current_scene = ""


    def run (self) :
        engine_globals.engine_state = self.initial_scene.name
        while (engine_globals.engine_state != engine_globals.STATE_ENUMS[0] and
                engine_globals.engine_state != engine_globals.STATE_ENUMS[3]) :
            if engine_globals.engine_state == self.initial_scene.name:
                self.initial_scene.display()
            for scene_name, scene_data in self.scenes.items():
                if engine_globals.engine_state == scene_name:
                    scene_data.display()