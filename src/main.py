from dialogmanager import DialogManager
from patterns import Patterns
from potion import Potion
from frame import Frame
from answer import Answer
import spacy
import time

nlp = spacy.load('it_core_news_sm') # load spacy model for italian
f = Frame()
dm = DialogManager()
pat = Patterns()
ans = Answer()

f.set_potion_name('Pozione Polisucco')
doc = nlp("La risposta esatta è le mosche Crisopa.") 

# Mesure performance of method find_ing_by_copula
start = time.time() 
asw = dm.find_ing_by_copula(doc)
end = time.time()
print(f"The copula approach takes {end - start} seconds")

f.check_response(asw)   
print(f"Right ingredients: {f.get_student_ingredients()}")

# TODO: fare un bel ciclo for per togliere tutte queste stampe ripetitive
# Mesure performance of method get_matched_patterns with different patterns
start = time.time()
print(dm.get_matched_patterns("aux_pattern", pat.pat_1, ans.ans_1)) 
print(dm.get_matched_patterns("aux_pattern", pat.pat_1, ans.ans_2))
print(dm.get_matched_patterns("aux_pattern", pat.pat_1, ans.ans_3))
end = time.time()
print(f"The matched_patterns method takes {end - start} seconds")

# Mesure performance of method get_matched_patterns_from_dependency with different patterns
start = time.time()
print(dm.get_matched_patterns_from_dependency("aux_pattern", pat.pat_2, ans.ans_1)) 
print(dm.get_matched_patterns_from_dependency("aux_pattern", pat.pat_3, ans.ans_2))
print(dm.get_matched_patterns_from_dependency("aux_pattern", pat.pat_2, ans.ans_3))
print(dm.get_matched_patterns_from_dependency("aux_pattern", pat.passive_pat, ans.ans_4))
print(dm.get_matched_patterns_from_dependency("aux_pattern", pat.passive_pat, ans.ans_5))
print(dm.get_matched_patterns_from_dependency("aux_pattern", pat.passive_pat, ans.ans_6))
end = time.time()
print(f"The matched_patterns_from_dependency takes {end - start} secondi :)")