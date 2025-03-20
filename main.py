from src.module_utils import module_editor, module_loader
from src.module_utils.module_editor import ModuleCreator
from src.utils import engine_globals, menu_functions
from src.utils import data_management

MAIN_MENU_OPTIONS = {
    "1": menu_functions.new_game_menu,
    "2": menu_functions.options_menu,
    "3": menu_functions.main_menu_exit,
    }

module_editor_class : ModuleCreator

def MainThread  ():
    """Main state handling function. Handles all code."""

    module_editor_class = module_editor.new_module_editor()

    engine_globals.init()

    engine_globals.engine_state = engine_globals.STATE_ENUMS[0]
    print("Welcome to " 
          + engine_globals.PROGRAM_NAME + ".")
    print("Created by: " 
          + engine_globals.CREATOR_NAME)
    while engine_globals.engine_state != engine_globals.STATE_ENUMS[3]:
        if engine_globals.engine_state == engine_globals.STATE_ENUMS[0]: # Main menu
            print(engine_globals.LINE_SEPERATOR_SMALL 
                  + "MAIN MENU" 
                  + engine_globals.LINE_SEPERATOR_SMALL)
            print("1: New Game")
            print("2: Options")
            print("3: Exit")
            print(engine_globals.LINE_SEPERATOR_LARGE)
            output = menu_functions.MenuSelection(
                "To input a selection, enter the number associated with it:",
                MAIN_MENU_OPTIONS,
                )
            if output == engine_globals.SELECTION_DEBUG[1]:
                print("Please enter a valid option.")
            
        if engine_globals.engine_state == engine_globals.STATE_ENUMS[1]: # New game menu
            modules = []
            menu_items = {}
            menu_item_modules = {}

            for file in module_loader.GetFiles(engine_globals.MODULE_LOADER_PATH) :
                modules.append(module_loader.LoadFile(engine_globals.MODULE_LOADER_PATH, file))
            print(engine_globals.LINE_SEPERATOR_SMALL 
                  + engine_globals.STATE_ENUMS[1] 
                  + engine_globals.LINE_SEPERATOR_SMALL)
            module_index = 0
            for module in modules:
                print(str(module_index + 1) 
                      + ": " 
                      + module.name)
                menu_items[str(module_index + 1)] = module.run
                module_index += 1
            print(str(module_index + 1) 
                  + ": Return to main menu")
            menu_items[str(module_index + 1)] = menu_functions.return_to_main_menu
            output = menu_functions.MenuSelection(
                "Please select what module you would like to play: ",
                menu_items,
                {"", ""}
            )
        if engine_globals.engine_state == engine_globals.STATE_ENUMS[2]: # Options menu
            module_editor_class.module_editor()

    print("Exiting...")
    print("Goodbye")



MainThread ()