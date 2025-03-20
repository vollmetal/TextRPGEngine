
from ..module_utils.create_item_file import module_serializer
from .module import Module
from .module_loader import LoadModule, LoadModulesInDirectory
from ..utils import data_management, engine_globals
from ..utils.game_classes.item import Item
from ..utils.game_classes.world_functions.cell import Cell
from ..utils.game_classes.world_functions.world import Worldspace

class ModuleCreator:

    def main_menu(self, selected_module: int, selected_item: list[int]):
        """handles the main menu display and functionality"""
        print(engine_globals.LINE_SEPERATOR_SMALL 
                    + engine_globals.STATE_ENUMS[2] 
                    + engine_globals.LINE_SEPERATOR_SMALL)
        x = 1
        menu_item_list = []
        for menu in self.main_menu_inputs:
            print(f"{x}: {menu}")
            menu_item_list.append(menu)
            x += 1
        menu_input = input("Please enter the value of the option you want: ")
        if  len(self.main_menu_inputs) >= int(menu_input) :
            self.current_menu_state = menu_item_list[(int(menu_input) - 1)]
        else:
            print(f"Please input a valid number for the menu option you would like to run.")
    
    # module handling
    def new_module(self, selected_module: int, selected_item: list[int]):
        """handles new module display and creation of new modules"""
        new_module_name = input("Please input the name of the new module: ")
        new_module_serializer = module_serializer(engine_globals.MODULE_STRUCTURE_PATH)
        new_module_serializer.serialize_module(new_module_name, engine_globals.MODULE_LOADER_PATH)
        new_module = Module(new_module_name)

        answer = input(f"Would you like to start editing {new_module_name} now? (y/yes for yes, n/no for no): ")
        if (answer == "yes") | (answer == "y"):
            self.current_menu_state = "edit module"
            self.module_container = []
            self.module_container.append(new_module)
            self.current_selected_module = 0
        else:
            self.current_menu_state = "main menu"

    def select_module(self, selected_module: int, selected_item: list[int]):
        """handles selecting a currently existing module"""
        
        print(f"{engine_globals.LINE_SEPERATOR_SMALL}\nSelect What Module to Load\n{engine_globals.LINE_SEPERATOR_SMALL}")
        loaded_modules = LoadModulesInDirectory(engine_globals.MODULE_LOADER_PATH)
        x = 0
        for found_module in loaded_modules:
            print(f'{x}: {found_module.name}')
            x += 1
        edit_module_inputs = {
             x: "main menu"
            }
        for base_menu_input in edit_module_inputs:
            print(f"{x + 1}: {base_menu_input}")
        user_input = input("")
        if int(user_input) in edit_module_inputs.keys:
            self.current_menu_state = edit_module_inputs[user_input - 1]
        else:
            if int(user_input) - 1 <= len(loaded_modules):
                self.current_menu_state = 'edit module'
                self.current_selected_module = loaded_modules[int(user_input) - 1]
            else:
                print('Please enter a valid menu item number. Valid menu item numbers are the numbers next to each menu item.')
            
    def edit_module(self, selected_module: int, selected_item: list[int]):
        """handles the editing of a selected module"""
        edit_module_inputs = [
            "new item",
            "new cell",
            "new worldspace",
            "main menu"
            ]
        print(f"{engine_globals.LINE_SEPERATOR_SMALL}\nSelect What to do With {self.module_container[self.current_selected_module].name}\n{engine_globals.LINE_SEPERATOR_SMALL}")
        x = 0
        for base_menu_input in edit_module_inputs:
            print(f"{x + 1}: {base_menu_input}")
            x += 1
        user_input = input("")
        self.current_menu_state = edit_module_inputs[str(user_input) - 1]
         

    # item handling
    def new_item(self, selected_module: int, selected_item: list[int]):
        """handles the creation of new items"""
        pass

    def select_item(self, selected_module: int, selected_item: list[int]):
        """handles the menu for selecting a currently existing item"""
        pass

    def edit_item(self, selected_module: int, selected_item: list[int]):
        pass

    # worldspace handling
    
    def new_worldspace(self, selected_module: int, selected_item: list[int]):
        pass

    def select_worldspace(self, selected_module: int, selected_item: list[int]):
        pass

    # cell handling

    def new_cell(self, selected_module: int, selected_item: list[int]):
        pass

    def select_cell(self, selected_module: int, selected_item: list[int]):
        pass
    
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
            "new worldspace": self.new_worldspace,
            "new cell": self.new_cell,
            "edit item": self.edit_item,
            "select item": self.select_item,
            "select worldspace": self.select_worldspace,
            "select cell": self.select_cell
        }
        """contains the different menus.\n 
        Format is: {name: menu function}"""

        self.module_container = [Module]
        self.object_container = {"items": [Item],
                                 "worldspace": [Worldspace],
                                 "cells": [Cell]
                                 }

        self.current_selected_module = -1
        self.current_selected_items = [-1]
        

    def module_editor(self):
        """the handler to cycle through different parts of the module editor"""
        if self.current_menu_state != "exit":
            if self.current_menu_state in self.me_menus:
                self.me_menus[self.current_menu_state](self.current_selected_module, self.current_selected_items)
        else:
            engine_globals.engine_state = engine_globals.STATE_ENUMS[0]
    

def new_module_editor():
    instance = ModuleCreator()
    return instance