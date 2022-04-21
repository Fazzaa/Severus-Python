from potion import Potion

class Frame:

    def __init__(self):
        self.potions = {}
        self.student_ingredients = [] # memorizza le risposte corrette (ingredienti) dello studente
        self.potion_name = "" # il nome della pozione oggetto dell'interrogazione
        self.student_name = ""
        self.student_potion_name = "" #! domanda infame: ti chiedo il nome della pozione dandoti gli ingredienti
        self.add_potions()
        self.mood = 0 # from 0 to 10 (0 = happy, 10 = angry)

    def get_potion_name(self):
        return self.potion_name

    def set_potion_name(self, potion_name):
        self.potion_name = potion_name
    
    def get_student_ingredients(self):
        return self.student_ingredients

    def get_student_name(self):
        return self.student_name

    def set_student_name(self, student_name):
        self.student_name = student_name

    def get_mood(self):
        return self.mood

    def set_mood(self, mood):
        self.mood = mood
    
    # aggiungo la lista di pozioni al dizionario del frame leggendole da potions.txt
    def add_potions(self):
        file = open("/home/andrea/Desktop/Università/TLN/Parte 1/Severus-Python/data/potions.txt", "r")
        for line in file:
            p = list(line.strip("\n").split(','))
            p_name = p[0]
            p_ing = p[1:]
            self.potions[p_name] = p_ing
    
    def to_string(self):
        res = ""
        res = f"{res}Pozione scelta per l'interrogazione: {self.potion_name}\n" \
              f"Studente interrogato: {self.student_name}\n"\
              f"Elenco pozioni conosciute:\n"

        for p in self.potions.keys():
            res += f"{p}, ingredienti: {self.potions[p]} \n"
        return res

    # controllo che l'ingrediente sia corretto e se lo è lo aggiungo alle risposte corrette (se non è già stato detto)
    #TODO:lavorare su stemming e rimozioni parti non necessarie 
    def check_response(self, ingredient):
        for i in self.potions[self.potion_name]:
            if i.lower() == ingredient.lower()  and (i not in self.student_ingredients):
                self.student_ingredients.append(i)
                return True
        return False


#TESTING
f = Frame()

f.set_potion_name("Pozione Polisucco") #Estratta a caso

f.check_response("mosche crisopa")
f.check_response("mosche crisopa")

print(f.get_student_ingredients())


