from ... import utils
from .. import engine_classes

class Item:
    """base item class holding all basic properties and functions"""

    name: str
    """the item's name"""

    size: utils.engine_classes.Vector3D
    """object size in milimeters"""

    weight: int
    """object weight in grams"""

    value: int 
    """cost of item"""

    icon: str
    """path to icon or character (for ascii graphics)"""

    category: str

    keywords: list[str]

    crafting_recipes: {str}

    def __init__ (self, name: str, size: engine_classes.Vector3D, weight: int, value: int, icon: str, category: str, keywords: list[str], crafting_recipes: {str}) :
        self.name = name
        self.size = size
        self.weight = weight
        self.value = value
        self.icon = icon
        self.category = category
        self.keywords = keywords
        self.crafting_recipes = crafting_recipes

    def __str__(self):
        return f'{self.name}\nsize:(width: {self.size.x}, height: {self.size.y}, length: {self.size.z})\nweight: {self.weight}\nvalue: {self.value}\nsorted into category: {self.category}\ncontains keywords: {self.keywords}'
    
    def serialize(self) -> dict[str]:
        serialized_output = {}
        serialized_output['name'] = self.name
        serialized_output['size'] = self.size
        serialized_output['weight'] = self.size
        serialized_output['value'] = self.value
        serialized_output['icon'] = self.icon
        serialized_output['category'] = self.category
        serialized_output['keywords'] = self.keywords
        serialized_output['crafting_recipes'] = self.crafting_recipes

    
    
    # keyword functions

    def add_keyword (self, keyword: str):
        """appends a keyword to the end of the list of keywords"""
        self.keywords.append(keyword)

    def remove_keyword(self, id:int):
        """unregisters a keyword with the input id"""
        try: 
            del self.keywords[id]
        except:
            print("ERROR KEYWORD NOT FOUND")

    # crafting recipe functions

    def add_crafting_recipe(self, id:str, crafting_recipe):
        """adds a single crafting recipe with the id string as a key"""
        self.crafting_recipes[id] = crafting_recipe
    
    def remove_crafting_recipe(self, id:str):
        """unregisters a crafting recipe with the input id"""
        try: 
            del self.crafting_recipes[id]
        except:
            print("ERROR RECIPE NOT FOUND")