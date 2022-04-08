from potion import Potion

class Frame:

    def __init__(self, list_of_potions):
        self.potions = {}
        self.nome_interrogato = ""
        self.add_potions(list_of_potions)
    
    # aggiungo la lista di pozioni al dizionario del frame
    def add_potions(self, list_of_potions):
        for potion in list_of_potions:
            self.potions[potion.get_potion_name()] = potion.get_ingredients()
    
    def to_string(self):
        res = ""
        for i in self.potions.keys():
            res += f"Ricette: {i} con ingredienti {self.potions[i]}\n"
        return res
'''
    def check_response(self, ingredient):
        for value in self.ingredients.values():
            if value[0] == ingredient:
                return value[1]

    #*setto a True l'ingrediente passato come parametro
    def set_ingredient(self, ingredient):
        for value in self.ingredients.values():
            if value[0] == ingredient:
                value[1] = True

    #*restituisce il primo ingrediente non ancora dichiarato dall'utente (False)
    def get_ingredient(self):
        for value in self.ingredients.values():
            if value[1] == False:
                return value[0]
        return "No more ingredients"
'''
potions = []
potions.append(Potion("Pozione Polissucchio", ["A","B","C"]))
potions.append(Potion("Pozione Invisibilità", ["D","E","F"]))
potions.append(Potion("Pozione Morte", ["G","H","I"]))

memoria_piton = Frame(potions)

print(memoria_piton.to_string())

