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

    use_functions: {str}

    def __init__ (self, name: str, size: engine_classes.Vector3D, weight: int, value: int, icon: str, category: str, keywords: list[str], crafting_recipes: {str}, use_functions: {str}) :
        self.name = name
        self.size = size
        self.weight = weight
        self.value = value
        self.icon = icon
        self.category = category
        self.keywords = keywords
        self.crafting_recipes = crafting_recipes
        self.use_functions = use_functions
    
    
    def get_name(self) -> str:
        return self.name
    
    # size functions
    def get_size (self) -> engine_classes.Vector3D:
        return self.size
    
    def set_size (self, size: engine_classes.Vector3D):
        self.size = size
    
    # weight functions
    def get_weight (self) -> int:
        return self.weight
    
    def set_weight (self, weight: int):
        self.weight = weight
    
    # value functions
    def get_value (self) -> int:
        return self.value
    
    def set_value (self, value: int):
        self.value = value
    
    # icon functions
    def get_icon (self) -> str:
        return self.icon
    
    def set_icon (self, icon: str):
        self.icon = icon

    # category functions
    def get_category(self) -> str:
        return self.category
    
    def set_category (self, category: str):
        self.category = category

    # keyword functions
    def get_keywords (self) -> list[str]:
        return self.keywords

    def set_keywords (self, keywords: list[str]):
        self.keywords = keywords

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
    def get_crafting_recipes (self) -> {str}:
        """returns a dictionary of registered crafting recipes"""
        return self.crafting_recipes

    def set_crafting_recipes (self, crafting_recipes: {str}):
        """sets the crafting recipes for the item to the input dictionary"""
        self.crafting_recipes = crafting_recipes

    def add_crafting_recipe(self, id:str, crafting_recipe):
        """adds a single crafting recipe with the id string as a key"""
        self.crafting_recipes[id] = crafting_recipe
    
    def remove_crafting_recipe(self, id:str):
        """unregisters a crafting recipe with the input id"""
        try: 
            del self.crafting_recipes[id]
        except:
            print("ERROR RECIPE NOT FOUND")

    def use_item(self, id: str, *args):
        """uses any one of the functions registered with the item denoted by the input id. Args is a tuple of any inputs the function may require."""
        self.use_functions[id](args)