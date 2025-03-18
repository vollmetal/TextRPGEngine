from src import eng_globals


class Scene:
    name: str
    """name of the scene"""

    description: str
    """The text of the scene"""

    user_inputs: dict[str]
    """The different user inputs and their functions in this order:
    {name: str,
     {"text": input text,
     "value": values to be used for the input function,
     "type": what function will be called for this input}
     """

    def __init__ (self, new_name: str, new_desc: str):
        self.name = new_name
        self.description = new_desc
        self.user_inputs = {}

    def add_user_input (self, new_inputs: dict[str]):
        """imports new user inputs from a dictionary
        new_inputs: contains all new user inputs for the scene
        """
        for key, value in new_inputs.items():
            input_name = key
            self.user_inputs[input_name] = {}
            input_data = value
            for key, value in input_data.items():
                match key:
                    case "text":
                        self.user_inputs[input_name]["text"] = value
                    case "value":
                        self.user_inputs[input_name]["value"] = value
                    case "type":
                        self.user_inputs[input_name]["type"] = getattr(self, value)

    def display (self) :
        """main display thread"""
        print(eng_globals.LINE_SEPERATOR_SMALL 
              + self.name 
              + eng_globals.LINE_SEPERATOR_SMALL)
        print(self.description)
        print(eng_globals.LINE_SEPERATOR_SMALL 
              + "Inputs" 
              + eng_globals.LINE_SEPERATOR_SMALL)
        for key, action in self.user_inputs.items():
            print(key 
                  + ": " 
                  + action["text"])
        user_input = input("Select option: ")
        for key, action in self.user_inputs.items():
            if user_input == key:
                action["type"](action["value"])
        

    def scene_transfer (self, value):
        """changes the displayed scene to the value"""
        eng_globals.engine_state = value

    def exit_game (self, value):
        """exits to main menu"""
        eng_globals.engine_state = eng_globals.STATE_ENUMS[0]