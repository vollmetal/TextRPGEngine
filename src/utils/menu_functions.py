from ..utils import engine_globals, engine_classes

def new_game_menu ():
    
    engine_globals.engine_state = engine_globals.STATE_ENUMS[1]

def options_menu ():
    
    engine_globals.engine_state = engine_globals.STATE_ENUMS[2]

def main_menu_exit () :
    
    engine_globals.engine_state = engine_globals.STATE_ENUMS[3]

def return_to_main_menu () :
    
    engine_globals.engine_state = engine_globals.STATE_ENUMS[0]


def MenuSelection (state_text: str, functions: dict, *args: dict[str]):
    """Handles menu item selection.
    functions optionally holds functions to be run based on entries
    """

    user_choice = input(state_text)
    if functions.get(user_choice) != None:
        if len(args) > 0:
            for arg in args:
                if user_choice in arg:
                    functions[user_choice](arg.get(user_choice))
                    return engine_globals.SELECTION_DEBUG[0]
                else:
                    functions[user_choice]()
                    return engine_globals.SELECTION_DEBUG[0]
        else:
            functions[user_choice]()
            return engine_globals.SELECTION_DEBUG[0]
    else:
        return engine_globals.SELECTION_DEBUG[1]