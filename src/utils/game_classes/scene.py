

from typing import Callable
from ..game_classes.game_object import GameObject
from ...utils.user_input import handle_user_input


class Scene(GameObject):
    '''Holds a specific scene for display'''

    def __init__(self, name: str, text: str, input_options: dict[int: dict[str: str]]):
        super().__init__(name)
        print(self.name)
        self.text = text
        self.input_options = input_options
        '''Input options for the player, ordered as such:\n
        option int to check for,\n
        {\n
        message: message for player,\n
        scene: next scene name\n
        }
        '''
    def __str__(self):
        inherited_output = super().__str__()
        output = f'{inherited_output}\nText: {self.text}\nInputs: {self.input_options}'
        return output

    def run(self, player):
        print(self.text)
        for index, option in self.input_options.items():
            messsage = option['message']
            print(f'{index}: {messsage}')
        user_input = handle_user_input('', True, '', 'Please enter a valid input number.')
        if user_input is not None:
            user_input = int(user_input)
            if self.input_options.get(user_input) is not None:
                return self.input_options[user_input]['scene']
            else:
                return 'ERROR'
        else:
            return 'ERROR'
        
    def serialize(self) -> dict[str]:
        serialized_scene = super().serialize()
        serialized_scene['text'] = self.text
        serialized_scene['input options'] = self.input_options
        return serialized_scene
    

def deserialize(object_data) -> Scene | str:
    EXCEPTION_MESSAGE = 'Error loading object data. Please check json structure!'
    loaded_object = ''
    try:
        loaded_object = Scene(object_data['name'], object_data['text'], object_data['input options'])
    except:
        loaded_object = EXCEPTION_MESSAGE
    print(loaded_object)
    return loaded_object