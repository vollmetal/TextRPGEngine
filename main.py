from src import eng_globals
from src import module_loader
from src import menu_functions

MAIN_MENU_OPTIONS = {
    "1": menu_functions.new_game_menu,
    "2": menu_functions.options_menu,
    "3": menu_functions.main_menu_exit,
    }

def MainThread  ():
    """Main state handling function. Handles all code."""

    eng_globals.init()

    eng_globals.engine_state = eng_globals.STATE_ENUMS[0]
    print("Welcome to " 
          + eng_globals.PROGRAM_NAME + ".")
    print("Created by: " 
          + eng_globals.CREATOR_NAME)
    while eng_globals.engine_state != eng_globals.STATE_ENUMS[3]:
        if eng_globals.engine_state == eng_globals.STATE_ENUMS[0]: # Main menu
            print(eng_globals.LINE_SEPERATOR_SMALL 
                  + "MAIN MENU" 
                  + eng_globals.LINE_SEPERATOR_SMALL)
            print("1: New Game")
            print("2: Options")
            print("3: Exit")
            print(eng_globals.LINE_SEPERATOR_LARGE)
            output = menu_functions.MenuSelection(
                "To input a selection, enter the number associated with it:",
                MAIN_MENU_OPTIONS,
                )
            if output == eng_globals.SELECTION_DEBUG[1]:
                print("Please enter a valid option.")
            
        if eng_globals.engine_state == eng_globals.STATE_ENUMS[1]: # New game menu
            modules = []
            menu_items = {}
            menu_item_modules = {}

            for file in module_loader.GetFiles(eng_globals.MODULE_LOADER_PATH) :
                modules.append(module_loader.LoadFile(eng_globals.MODULE_LOADER_PATH, file))
            print(eng_globals.LINE_SEPERATOR_SMALL 
                  + eng_globals.STATE_ENUMS[1] 
                  + eng_globals.LINE_SEPERATOR_SMALL)
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
        if eng_globals.engine_state == eng_globals.STATE_ENUMS[2]: # Options menu
            print(eng_globals.LINE_SEPERATOR_SMALL 
                  + eng_globals.STATE_ENUMS[2] 
                  + eng_globals.LINE_SEPERATOR_SMALL)
            eng_globals.engine_state = eng_globals.STATE_ENUMS[3]
    print("Exiting...")
    print("Goodbye")

MainThread ()