class Frame:
    def __init__(self, potion_name):
        self.potion_name = potion_name
        self.ingredients = {}
        self.n_ingredients = 0
    
    def add_ingredient(self, ingredient):
        self.ingredients[self.n_ingredients] = [ingredient, False]
        self.n_ingredients += 1
    
    def to_string(self):
        return f"Ricetta: {self.potion_name} con ingredienti {self.ingredients}"

    def check_response(self, ingredient):
        for value in self.ingredients.values():
            if value[0] == ingredient:
                return value[1]

    #*setto a True l'ingrediente passato come parametro
    def set_ingredient(self, ingredient):
        for value in self.ingredients.values():
            if value[0] == ingredient:
                value[1] = True

    #!restituisce il primo ingrediente non ancora dichiarato dall'utente (False)
    def get_ingredient(self):
        for value in self.ingredients.values():
            if value[1] == False:
                return value[0]
        return "No more ingredients"