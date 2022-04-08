class Potion:
    def __init__(self, potion_name, ingredients):
        self.potion_name = potion_name
        self.ingredients = ingredients
        
    def get_potion_name(self):
        return self.potion_name
    
    def get_ingredients(self):
        return self.ingredients