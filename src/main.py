import random
from potion import Potion
from frame import Frame

#funzione che restituisce una frase randomica da una lista di frasi
def pick_random_start(phrases_list):
    return random.choice(phrases_list)