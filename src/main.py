from dialogmanager import DialogManager
from patterns import *
from frame import Frame
import spacy
import time

nlp = spacy.load('it_core_news_sm') # load spacy model for italian
f = Frame()
dm = DialogManager()

f.set_potion_name('Pozione Polisucco')
doc = nlp("La risposta esatta è le mosche Crisopa.") 

# TODO: fare un bel ciclo for per togliere tutte queste stampe ripetitive
# Mesure performance of method get_matched_patterns with different patterns
start = time.time()
print(dm.get_matched_patterns("pattern", pattern, "the answer is Crisopa Fly...")) 
print(dm.get_matched_patterns("pattern", pattern, "the potion contains Crisopa fly"))
print(dm.get_matched_patterns("pattern", pattern, "The first ingredient of the potion is the Crisopa fly"))
end = time.time()
print(f"The matched_patterns method takes {end - start} seconds")

# Mesure performance of method get_matched_patterns_from_dependency with different patterns
start = time.time()
print(dm.get_matched_patterns_from_dependency("pattern_aux", pattern_aux, "the answer is Crisopa Fly...")) 
print(dm.get_matched_patterns_from_dependency("pattern_verb", pattern_verb, "the potion contains Crisopa fly"))
print(dm.get_matched_patterns_from_dependency("pattern_aux", pattern_aux, "The first ingredient of the potion is the Crisopa fly"))
print(dm.get_matched_patterns_from_dependency("passive_pattern", passive_pattern, "Crisopa fly is used in the potion"))
print(dm.get_matched_patterns_from_dependency("passive_pattern", passive_pattern, "Crisopa Fly is needed in the potion"))
print(dm.get_matched_patterns_from_dependency("passive_pattern", passive_pattern, "I think that Crisopa Fly is needed in the potion"))
end = time.time()

print(f"The matched_patterns_from_dependency takes {end - start} secondi :)")