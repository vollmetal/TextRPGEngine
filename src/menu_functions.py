from src import eng_globals
from src import module

def new_game_menu ():
    
    eng_globals.engine_state = eng_globals.STATE_ENUMS[1]

def options_menu ():
    
    eng_globals.engine_state = eng_globals.STATE_ENUMS[2]

def main_menu_exit () :
    
    eng_globals.engine_state = eng_globals.STATE_ENUMS[3]

def return_to_main_menu () :
    
    eng_globals.engine_state = eng_globals.STATE_ENUMS[0]


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
                    return eng_globals.SELECTION_DEBUG[0]
                else:
                    functions[user_choice]()
                    return eng_globals.SELECTION_DEBUG[0]
        else:
            functions[user_choice]()
            return eng_globals.SELECTION_DEBUG[0]
    else:
        return eng_globals.SELECTION_DEBUG[1]