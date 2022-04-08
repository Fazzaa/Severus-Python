from potion import Potion

class Frame:

    def __init__(self, list_of_potions):
        self.potions = {} 
        self.student_ingredients = [] # memorizza gli ingredienti azzeccati dallo studente
        self.potion_name = "" # il nome della pozione oggetto dell'interrogazione
        self.student_name = ""
        self.student_potion_name = "" #! domanda infame: ti chiedo il nome della pozione dandoti gli ingredienti
        self.add_potions(list_of_potions)
        self.mood = 0 # from 0 to 10 (0 = happy, 10 = angry)

    def get_potion_name(self):
        return self.potion_name

    def set_potion_name(self, potion_name):
        self.potion_name = potion_name
    
    def get_student_name(self):
        return self.student_name

    def set_student_name(self, student_name):
        self.student_name = student_name

    def get_mood(self):
        return self.mood

    def set_mood(self, mood):
        self.mood = mood
    
    # aggiungo la lista di pozioni al dizionario del frame
    def add_potions(self, list_of_potions):
        for i in list_of_potions:
            self.potions[i.get_potion_name()] = i.get_ingredients()
    
    def to_string(self):
        res = ""
        res = f"{res}Pozione scelta per l'interrogazione: {self.potion_name}\n" \
              f"Studente interrogato: {self.student_name}\n"\
              f"Elenco pozioni conosciute:\n"

        for i in self.potions.keys():
            res += f"{i}, ingredienti: {self.potions[i]} \n"
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
potions.append(Potion("Pozione Polisucco", ["A","B","C"]))
potions.append(Potion("Pozione Invisibilità", ["D","E","F"]))
potions.append(Potion("Pozione Morte", ["G","H","I"]))

memoria_piton = Frame(potions)

print(memoria_piton.to_string())

