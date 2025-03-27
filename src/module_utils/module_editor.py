
from ..utils.user_input import handle_user_input
from ..utils.engine_classes import Vector3D
from ..module_utils.create_item_file import module_serializer
from .module import Module
from .module_loader import LoadModule, LoadModulesInDirectory
from ..utils import data_management, engine_globals
from ..utils.game_classes.item import Item
from ..utils.game_classes.world_functions.cell import Cell
from ..utils.game_classes.world_functions.world import Worldspace

class ModuleCreator:

    def main_menu(self, selected_module: int):
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
        new_module_name = input("Please input the name of the new module: ")
        new_module_serializer = module_serializer(engine_globals.MODULE_STRUCTURE_PATH)
        new_module_serializer.serialize_module(new_module_name, engine_globals.MODULE_LOADER_PATH)
        new_module = Module(new_module_name)

        input_prompt = f"Would you like to start editing {new_module_name} now? (y/yes for yes, n/no for no) default = no: "
        error_message = f"Please input a valid entry."
        answer = handle_user_input(input_prompt, False, "", error_message)
        if (answer == "yes") | (answer == "y"):
            self.current_menu_state = "edit module"
            self.module_container = []
            self.module_container.append(new_module)
            self.current_selected_module = 0
        else:
            self.current_menu_state = "main menu"

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
                self.current_selected_module = int(user_input)

            else:
                if (len(self.module_container)) == (int(user_input) - 1):
                    self.current_menu_state = 'main menu'
                else:
                    print(self.input_int_error)


    
            
    def edit_module(self, selected_module: int):
        """handles the editing of a selected module"""
        edit_module_inputs = [
            "new item",
            'select item',
            "new cell",
            "new worldspace",
            "main menu"
            ]
        print(self.module_container[self.current_selected_module])
        print(f"{engine_globals.LINE_SEPERATOR_SMALL}\nSelect What to do With {self.module_container[self.current_selected_module].name}\n{engine_globals.LINE_SEPERATOR_SMALL}")
        x = 0
        for base_menu_input in edit_module_inputs:
            print(f"{x + 1}: {base_menu_input}")
            x += 1
        user_input = handle_user_input(self.input_int_message, True, '', self.input_int_error)
        self.current_menu_state = edit_module_inputs[int(user_input) - 1]
         

    # item handling
    def new_item(self, selected_module: int):
        """handles the creation of new items"""
        process_position = 'name'
        item_size = Vector3D(0, 0, 0)
        new_module_serializer = module_serializer(engine_globals.MODULE_STRUCTURE_PATH)
        while process_position != 'finished':
            match process_position:
                case 'name':
                    item_name = input('What do you want to call this item?')
                    process_position = 'size'
                case 'size':
                    item_length = input('please enter the length of the item. Leave blank for 0.')
                    if item_length != '':
                        if item_length.isdigit():
                            item_size.x = int(item_length)
                        else:
                            pass
                    else:
                        pass
                    item_width = input('please enter the width of the item. Leave blank for 0.')
                    if item_width != '':
                        if item_width.isdigit():
                            item_size.z = int(item_width)
                        else:
                            pass
                    else:
                        pass
                    item_height = input('please enter the height of the item. Leave blank for 0.')
                    if item_height != '':
                        if item_height.isdigit():
                            item_size.y = int(item_height)
                        else:
                            pass
                    else:
                        pass
                    process_position = 'weight'
                case 'weight':
                    weight = input('please enter the weight of the item. Leave blank for 0.')
                    if weight.isdigit() or (weight == ''):
                        item_weight = weight
                        process_position = 'value'
                    else:
                        print('please enter a valid weight or leave the input blank')
                case 'value':
                    value = input('please enter the value of the item. Leave blank for 0.')
                    if value.isdigit() or value == '':
                        item_value = weight
                        process_position = 'finalization'
                    else:
                        print('please enter a valid value or leave the input blank')
                case "finalization":
                    try:
                        new_item = Item(item_name, item_size, item_weight, item_value, '', '', [], {}, {})
                        new_module_serializer.serialize_item(new_item, f'{engine_globals.MODULE_LOADER_PATH}/{self.module_container[self.current_selected_module].name}')
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
        for name, item in module.items.items():
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
            if int(user_input) - 1 <= len(self.module_container[self.current_selected_module].items):
                self.current_menu_state = 'edit item'
                self.current_selected_items = item_list[int(user_input) - 1]
                print(self.module_container[self.current_selected_module].items[self.current_selected_items])
            else:
                print(self.input_int_error)

    def edit_item(self, selected_module: int):
        print(f"{engine_globals.LINE_SEPERATOR_SMALL}\nEditing {self.module_container[self.current_selected_module].items[self.current_selected_items].name}\n{engine_globals.LINE_SEPERATOR_SMALL}")
        print(f'{self.module_container[self.current_selected_module].items[self.current_selected_items]}')
        print(f'{engine_globals.LINE_SEPERATOR_LARGE}')
        self.current_menu_state = 'edit module'

    # worldspace handling
    
    def new_worldspace(self, selected_module: int):
        pass

    def select_worldspace(self, selected_module: int):
        pass

    # cell handling

    def new_cell(self, selected_module: int):
        pass

    def select_cell(self, selected_module: int):
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
        self.current_selected_items = list[int]

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