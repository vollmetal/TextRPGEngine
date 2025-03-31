
from ...game_classes.scene import Scene
from ...game_classes.item import Item
from ...game_classes.game_object import GameObject
from ...user_input import handle_user_input
from ...engine_classes import Vector3D
from .serialize_object_funcs import module_serializer
from .module import Module
from .module_loader import LoadModule, LoadModulesInDirectory
from ....utils import engine_globals

class ModuleCreator:

    def main_menu(self, selected_module: int):
        """handles the main menu display and functionality"""
        print(engine_globals.LINE_SEPERATOR_SMALL 
                    + engine_globals.STATE_ENUMS[2] 
                    + engine_globals.LINE_SEPERATOR_SMALL)
        x = 1
        self.module_changed = False
        self.scene_changed = False
        menu_item_list = []
        for menu in self.main_menu_inputs:
            print(f"{x}: {menu}")
            menu_item_list.append(menu)
            x += 1
        
        error_message = f"Please input a valid number for the menu option you would like to run."
        menu_input = handle_user_input(self.input_int_message, True, "", self.input_int_error)
        if menu_input == None:
            pass
        else:
            if  len(self.main_menu_inputs) >= int(menu_input) :
                self.current_menu_state = menu_item_list[(int(menu_input) - 1)]
            else:
                print(self.input_int_error)
    
    # module handling
    def new_module(self, selected_module: int):
        """handles new module display and creation of new modules"""
        new_module_name = handle_user_input("Please input the name of the new module: ", False, '', self.input_int_error)
        new_module_version = handle_user_input(f"Please input the version of {new_module_name}: ", False, '', self.input_int_error)
        new_module_author = handle_user_input(f"Please input the name of {new_module_name}'s author: ", False, '', self.input_int_error)
        
        new_module = Module(new_module_name, '', new_module_version, new_module_author)

        input_prompt = f"Would you like to start editing {new_module_name} now? (y/yes for yes, n/no for no) default = no: "
        error_message = f"Please input a valid entry."
        answer = handle_user_input(input_prompt, False, "", error_message)
        if (answer == "yes") | (answer == "y"):
            self.current_menu_state = "edit module"
            self.module_container = []
            self.module_container.append(new_module)
            self.current_selected_module = 0
            self.module_changed = True
        else:
            self.current_menu_state = "main menu"
            self.module_serializer.serialize_module(new_module.serialize(), engine_globals.MODULE_LOADER_PATH)

    def select_module(self, selected_module: int):
        """handles selecting a currently existing module"""
        
        print(f"{engine_globals.LINE_SEPERATOR_SMALL}\nSelect What Module to Load\n{engine_globals.LINE_SEPERATOR_SMALL}")
        loaded_modules = LoadModulesInDirectory(engine_globals.MODULE_LOADER_PATH)
        
        self.module_container = loaded_modules
        x = 1
        for found_module in loaded_modules:
            print(f'{x}: {found_module.name}')
            x += 1
        edit_module_inputs = {
             x: "main menu"
            }
        for base_menu_input in edit_module_inputs.values():
            print(f"{x}: {base_menu_input}")
        user_input = handle_user_input(self.input_int_message, True, '', self.input_int_error)
        if user_input == None:
            pass
        else:
            if  len(self.module_container) > (int(user_input) - 1) :
                self.current_menu_state = 'edit module'
                self.current_selected_module = int(user_input) - 1

            else:
                if (len(self.module_container)) == (int(user_input) - 1):
                    self.current_menu_state = 'main menu'
                else:
                    print(self.input_int_error)


    
            
    def edit_module(self, selected_module: int):
        """handles the editing of a selected module"""
        edit_module_inputs = [
            'edit version number',
            'set initial scene',
            "new scene",
            'select scene',
            "main menu"
            ]
        print(f"{engine_globals.LINE_SEPERATOR_SMALL}\nSelect What to do With {self.module_container[self.current_selected_module].name}\n{engine_globals.LINE_SEPERATOR_SMALL}")
        current_module = self.module_container[self.current_selected_module]
        x = 0
        for base_menu_input in edit_module_inputs:
            print(f"{x + 1}: {base_menu_input}")
            x += 1
        user_input = handle_user_input(self.input_int_message, True, '', self.input_int_error)
        match user_input:
            case None:
                print('ERROR')
            case '1':
                new_version_number = handle_user_input(f'Please input a new version number. Type back to return to previous menu:\n ', False, '', self.input_int_error)
                if new_version_number != None:
                    if new_version_number.lower() is 'back':
                        pass
                    else:
                        self.module_container[self.current_selected_module].version_number = new_version_number
                        self.module_changed = True
            case '2':
                print(f"{engine_globals.LINE_SEPERATOR_SMALL}\nPlease select which scene to start with\n{engine_globals.LINE_SEPERATOR_SMALL}")
                selecting = True
                while selecting == True:
                    x = 1
                    scene_list = []
                    for name, scene in current_module.scene_dict.items():
                        scene_list.append(name)
                        print(f'{x}: {name}')
                        x += 1
                    selection_inputs = {
                        x: "back"
                        }
                    for slection_input in selection_inputs.values():
                        print(f"{x}: {slection_input}")
                    user_select_input = handle_user_input(f'', True, '', self.input_int_error)
                    user_selection_int = int(user_select_input) - 1
                    if (user_selection_int + 1) in selection_inputs.keys():
                        selecting = False
                    else:
                        if user_selection_int <= len(scene_list):
                            current_module.start_scene = scene_list[user_selection_int]
                            selecting = False
                            self.module_changed = True
                        else:
                            print(f'please input a valid selection')
                
            case _:
                self.current_menu_state = edit_module_inputs[int(user_input) - 1]
        if self.current_menu_state is "main menu":
            if self.module_changed:
                self.serialize_module_changes()
         

    # item handling
    def new_item(self, selected_module: int):
        """handles the creation of new items"""
        process_position = 'name'
        name_input_message = f'Please input the name of the new object:\n'
        new_module_serializer = module_serializer(engine_globals.MODULE_STRUCTURE_PATH)
        while process_position != 'finished':
            match process_position:
                case 'name':
                    item_name = handle_user_input(name_input_message, False, '', self.input_int_error)
                    print(item_name)
                    process_position = 'finalization'
                case "finalization":
                    try:
                        item_path = engine_globals.MODULE_STRUCTURE_PATH['items']
                        new_object = Item(item_name)
                        print(new_object)
                        print(f'path to check: {engine_globals.MODULE_LOADER_PATH}/{self.module_container[self.current_selected_module].name}/{item_path}/{new_object.name}')
                        new_module_serializer.serialize_object(
                            f'{engine_globals.MODULE_LOADER_PATH}/{self.module_container[self.current_selected_module].name}/{item_path}', 
                                                               new_object)
                    except:
                        print('ERROR WRITING MODULE')
                    process_position = 'finished'
        self.current_menu_state = 'edit module'


    def select_item(self, selected_module: int):
        """handles the menu for selecting a currently existing item"""
        print(f"{engine_globals.LINE_SEPERATOR_LARGE}\nSelect What Item to Edit\n{engine_globals.LINE_SEPERATOR_LARGE}")
        item_list = []
        module: Module = self.module_container[self.current_selected_module]
        x = 1
        for name, item in module.module_objects.items():
            item_list.append(item.name)
            print(f'{x}: {name}')
            x += 1
        edit_module_inputs = {
             x: "main menu"
            }
        for base_menu_input in edit_module_inputs.values():
            print(f"{x}: {base_menu_input}")
        user_input = handle_user_input(self.input_int_message, True, '', self.input_int_error)
        if int(user_input) in edit_module_inputs.keys():
            self.current_menu_state = edit_module_inputs[int(user_input)]
        else:
            if int(user_input) - 1 <= len(self.module_container[self.current_selected_module].module_objects):
                self.current_menu_state = 'edit item'
                self.current_selected_items = item_list[int(user_input) - 1]
                print(self.module_container[self.current_selected_module].module_objects[self.current_selected_items])
            else:
                print(self.input_int_error)

    def edit_item(self, selected_module: int):
        print(f"{engine_globals.LINE_SEPERATOR_SMALL}\nEditing {self.module_container[self.current_selected_module].module_objects[self.current_selected_items].name}\n{engine_globals.LINE_SEPERATOR_SMALL}")
        print(f'{self.module_container[self.current_selected_module].module_objects[self.current_selected_items]}')
        print(f'{engine_globals.LINE_SEPERATOR_LARGE}')
        self.current_menu_state = 'edit module'

    # scene handling
    
    def new_scene(self, selected_module: int):
        print(f"{engine_globals.LINE_SEPERATOR_SMALL}\nCreating New Scene\n{engine_globals.LINE_SEPERATOR_SMALL}")
        self.object_container['scenes'] = []

        scene_name = handle_user_input(f'please enter a name for the scene:\n', False, '', self.input_int_error)
        scene_text = handle_user_input(f'please input the contents of the scene (you can manually add text into the "text" field in the .scene file if you want a more complex or longer scene):\n', False, '', self.input_int_error)
        scene_input_answer = handle_user_input(f'do you want to add a new scene input now?: y or yes to add one, otherwise it will make a scene with no answers\n', False, '', self.input_int_error)
        scene_input_dict = {}
        
        if (scene_input_answer.lower() == "yes") | (scene_input_answer.lower() == "y"):
            index = 1
            finished = False
            while finished == False:
                user_input_text = handle_user_input(f"please input the message for the scene's input", False, '', self.input_int_error)
                next_scene_name = handle_user_input(f'please input the name of a scene to point to:\n', False, '', self.input_int_error)
                scene_input_dict[index] = {user_input_text: next_scene_name}
                index += 1
                finish_answer = handle_user_input(f'finish adding new inputs?\n', False, '', self.input_int_error)
                if finish_answer is not None:
                    if (finish_answer.lower() == 'y') | (finish_answer.lower() == 'yes'):
                        finished = True
        new_scene = Scene(scene_name, scene_text, scene_input_dict)
        self.module_container[self.current_selected_module].scene_dict[new_scene.name] = new_scene
        input_prompt = f"Would you like to start editing {scene_name} now? (y/yes for yes): "
        error_message = f"Please input a valid entry."
        answer = handle_user_input(input_prompt, False, "", error_message)
        if (answer.lower() == "yes") | (answer.lower() == "y"):
            self.current_menu_state = "edit scene"
            self.object_container['scenes'].append(new_scene)
            self.current_selected_scene = 0
            self.scene_changed = True
        else:
            self.current_menu_state = "edit module"
            self.module_serializer.serialize_scene(engine_globals.MODULE_LOADER_PATH + '/' + self.module_container[self.current_selected_module].name + '/' + engine_globals.MODULE_STRUCTURE_PATH['scenes'], new_scene)

    def select_scene(self, selected_module: int):
        """handles the menu for selecting a currently existing scene"""
        print(f"{engine_globals.LINE_SEPERATOR_LARGE}\nSelect What Scene to Edit\n{engine_globals.LINE_SEPERATOR_LARGE}")
        self.object_container['scenes'] = []
        scene_list = []
        module: Module = self.module_container[self.current_selected_module]
        x = 1
        for name, scene in module.scene_dict.items():
            scene_list.append(scene.name)
            self.object_container['scenes'].append(scene)
            print(f'{x}: {name}')
            x += 1
        edit_module_inputs = {
             x: "main menu"
            }
        for base_menu_input in edit_module_inputs.values():
            print(f"{x}: {base_menu_input}")
        user_input = handle_user_input(self.input_int_message, True, '', self.input_int_error)
        if int(user_input) in edit_module_inputs.keys():
            self.current_menu_state = edit_module_inputs[int(user_input)]
        else:
            if int(user_input) - 1 <= len(self.module_container[self.current_selected_module].scene_dict):
                self.current_menu_state = 'edit scene'
                self.current_selected_scene_name = scene_list[int(user_input) - 1]
                self.current_selected_scene = int(user_input) - 1
                print(self.module_container[self.current_selected_module].scene_dict[self.current_selected_scene_name])
            else:
                print(self.input_int_error)

    def edit_scene(self, selected_module: int):
        current_scene = self.object_container['scenes'][self.current_selected_scene]
        print(f"{engine_globals.LINE_SEPERATOR_SMALL}\nEditing {current_scene.name}\n{engine_globals.LINE_SEPERATOR_SMALL}")
        print(current_scene)
        self.module_serializer.serialize_scene(engine_globals.MODULE_LOADER_PATH + '/' + self.module_container[self.current_selected_module].name + '/' + engine_globals.MODULE_STRUCTURE_PATH['scenes'], current_scene)
        self.current_menu_state = 'edit module'

    def serialize_module_changes(self):
        self.module_serializer.serialize_module(self.module_container[self.current_selected_module].serialize(), engine_globals.MODULE_LOADER_PATH)
    
    # ------------------------------------------------------------------------------------------------------------------------
    # initialization and main functions
    # ------------------------------------------------------------------------------------------------------------------------

    def __init__(self):
        self.current_menu_state = "main menu"
        self.main_menu_inputs = [
            "new module",
            "select module",
            "exit"
        ]
        self.me_menus = {
            "main menu": self.main_menu,
            "new module": self.new_module,
            "select module": self.select_module,
            "edit module": self.edit_module,      
            "new item": self.new_item,
            "edit item": self.edit_item,
            "select item": self.select_item,
            'new scene': self.new_scene,
            'select scene': self.select_scene,
            'edit scene': self.edit_scene
        }
        """contains the different menus.\n 
        Format is: {name: menu function}"""

        self.module_container = [Module]
        self.object_container = {"items": [],
                                 'scenes': []
                                 }
        
        self.module_changed = False
        self.scene_changed = False

        self.current_selected_module = -1
        self.current_selected_scene = -1
        self.current_selected_items = list[int]

        self.module_serializer = module_serializer(engine_globals.MODULE_STRUCTURE_PATH)
        self.input_int_message = "Please enter the number corresponding to your chosen menu option: \n"
        self.input_int_error = 'Please enter a valid menu item number. Valid menu item numbers are the numbers next to each menu item.'
        

    def module_editor(self):
        """the handler to cycle through different parts of the module editor"""
        if self.current_menu_state != "exit":
            if self.current_menu_state in self.me_menus:
                self.me_menus[self.current_menu_state](self.current_selected_module)
        else:
            engine_globals.engine_state = engine_globals.STATE_ENUMS[0]
    

def new_module_editor():
    instance = ModuleCreator()
    return instance