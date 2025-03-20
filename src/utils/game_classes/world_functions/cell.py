from ..item import Item
from ..entity import Entity

class Cell: 

    name: str
    items: dict[str, Item]
    entity: Entity
    move_cost: int

    def __init__(self, name: str, items: dict[str, Item] = {}, entity: Entity = {}, move_cost: int = 0):
        self.name = name
        self.items = items
        self.entity = entity
        self.move_cost = move_cost

    def __str__(self):
        return_string = f""
        if self.entity != None:
            return_string = (f"""Cell: {self.name}, """
                             f"""contains items: {self.items}, """
                             f"""and has no one in it.""")
        else:
            return_string =  (f"""Cell: {self.name}, """
                             f"""contains items: {self.items}, """
                             f"""and has {self.entity.name} in it.""")
        return return_string
    
    # item functions
    
    def add_item (self, item: Item):
        self.name[item.name] = item
            
    #entity functions

    #movement functions