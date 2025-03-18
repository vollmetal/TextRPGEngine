import src
from src.scene_branch import Scene
from src import eng_globals
from src import menu_functions

class Module:
    name: str

    scenes: dict[str : Scene]

    initial_scene: Scene

    current_scene: str

    def __init__ (self, name: str) :
        self.name = name
        self.scenes = {}
        self.initial_scene = Scene
        self.current_scene = ""

    def add_scenes (self, scene_name : str, scene : Scene, initial_scene: bool) :
        if initial_scene:
            self.initial_scene = scene
            self.current_scene = scene.name
        else:
            self.scenes[scene_name] = scene

    def run (self) :
        eng_globals.engine_state = self.initial_scene.name
        while (eng_globals.engine_state != eng_globals.STATE_ENUMS[0] and
                eng_globals.engine_state != eng_globals.STATE_ENUMS[3]) :
            if eng_globals.engine_state == self.initial_scene.name:
                self.initial_scene.display()
            for scene_name, scene_data in self.scenes.items():
                if eng_globals.engine_state == scene_name:
                    scene_data.display()