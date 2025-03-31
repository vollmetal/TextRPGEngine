


from .game_object import GameObject


class Item(GameObject):


    def __init__(self, name: str, weight: int, value: int, volume: int):
        super().__init__(name)
        self.weight = weight
        self.value = value
        self.volume = volume

    def __str__(self):
        main_string = super().__str__()
        return f'{main_string}\nweighs: {self.weight}\nhas a value of: {self.value}\nhas a volume of: {self.volume}'

    def serialize(self):
        serialized_object = super().serialize()
        serialized_object['weight'] = self.weight
        serialized_object['value'] = self.value
        serialized_object['volume'] = self.volume

def deserialize(object_data) -> Item | str:
    EXCEPTION_MESSAGE = f'Error loading object data. Please check json structure!\n loaded object from json: {object_data}'
    loaded_object = ''
    try:
        loaded_object = Item(object_data['name'], object_data['weight'], object_data['value'], object_data['volume'])
    except:
        loaded_object = EXCEPTION_MESSAGE
    return loaded_object