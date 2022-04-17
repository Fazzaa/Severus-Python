import random
import time
from potion import Potion
from frame import Frame
import spacy
# from nltk import Tree
#from spacy.symbols import cop
from nltk.stem import SnowballStemmer


#HINT1: SE AUX È PRESENTE -> INGREDIENTE È COPULA DI AUX
#HINT2: SE VERB È PRESENTE -> INGREDIENTE NSUBJ DI VERB
#HINT3: SE NON È PRESENTE NE VERB NE AUX -> È TUTTO INGREDIENTE

#funzione che restituisce una frase randomica da una lista di frasi
def pick_random_start(phrases_list):
    return random.choice(phrases_list)

nlp = spacy.load('it_core_news_sm')

#Cerca la copula nella frase, se è presente salva la parte successiva come ingrediente (HINT1)
def find_ing_by_copula(sentence):
    answer = ""
    start_copy = False
    for token in sentence:
        if start_copy:
            if token.dep_ != 'det' and not token.is_punct:
                answer += " " + token.text
        if token.dep_ == 'cop':
            start_copy = True
    return answer.strip()

f = Frame()
f.set_potion_name('Pozione Polisucco')
doc = nlp("La risposta esatta è le mosche Crisopa.") 

#! per capire quale funzione è più veloce
start1 = time.time() 
asw = find_ing_by_copula(doc)
end1 = time.time()
print(f"metodo 1 ci mette {end1 - start1} secondi :(")

f.check_response(asw)   
print(f"Ingredienti giusti: {f.get_student_ingredients()}")

'''----------------------------------------------------------------------------------------------------------------------'''
#* Alternativa con matcher per riconoscere il pattern:
# matcher spacy http://spacy.pythonhumanities.com/02_02_matcher.html#
# si utlizza la stessa funzione per riconoscere i vari pattern, si possono così
# creare più pattern da usare a seconda della parola senza dover fare 50 funzioni

import spacy
from spacy.matcher import Matcher

nlp = spacy.load('en_core_web_sm')

def get_matched_patterns(name_pattern, pattern, text):
    # funzione che usa il matcher di spacy per riconoscere il pattern passato come parametro in un testo
    # ordina gli elementi che fanno match col pattern e poi restituisce una lista di frasi che lo soddisfano
    matched_elements = [] 
    matcher = Matcher(nlp.vocab)
    matcher.add(name_pattern, [pattern], greedy="LONGEST")
    doc = nlp(text)
    matches = matcher(doc)
    matches.sort(key = lambda x : x[1])
    matched_elements = [(nlp.vocab[matches[0][0]].text, doc[match[1]:match[2]][1:]) for match in matches] 
    #[1:] perchè il primo elemento è l'ausiliare che non voglio nella lista
    # stampati matches e vedrai che queste oeprazioni avranno senso
    return matched_elements

pattern = [
    #{"LEMMA" : {"IN" : ["be", "contain", "use", "need", "have"]}},
    {"DEP" : "ROOT"},
    {"IS_ALPHA" : True, "OP": "+"}
]

answer1 = "the answer is Crisopa Fly..."
answer2 = "the potion contains Crisopa fly"
answer3 = "The first ingredient of the postion is the Crisopa fly"

start2 = time.time()
print(get_matched_patterns("aux_pattern", pattern, answer1)) 
print(get_matched_patterns("aux_pattern", pattern, answer2))
print(get_matched_patterns("aux_pattern", pattern, answer3))
end2 = time.time()



print(f"metodo 2 ci mette {end2 - start2} secondi :)")


'''
implementare modo per togliere l'articolo dalla frase matchata, si può fare direttamente nel frame nella funzione check_response
così il match è più facile e si ottengono informazioni belle
'''


'''----------------------------------------------------------------------------------------------------------------------'''
#* Alternativa con dependency matcher per riconoscere il pattern


#*DISCLAIMER: i nomi dei pattern e dei vari attributi sono opinabili, lo so. Sentitevi liberi di cambiarli.

from spacy.matcher import DependencyMatcher

#TODO: riuscire a passare in input una lista di patter (?) e magari una lista di nomi di pattern associati 
#TODO: (in modo da riuscire a capire quale pattern ha fatto match e avere il nome del pattern)
def get_matched_patterns_from_dependency(name_pattern, pattern, text):
    # funzione che usa il dependency matcher di spacy per riconoscere il pattern passato come parametro in un testo
    # ordina gli elementi che fanno match col pattern e poi restituisce una lista di frasi che lo soddisfano
    matched_elements = [] 
    matcher = DependencyMatcher(nlp.vocab)
    matcher.add(name_pattern, [pattern])
    doc = nlp(text)
    matches = matcher(doc)
    matches.sort(key = lambda x : x[1])
    #! Davvero scritta male, secondo me si può fare di meglio qui
    for match in matches:
        if match != []:
            match_words = match[1]
            if match_words[0] > match_words[1]: #! A volte vengono restituiti due indici, a volte 3, bisogna capire come restituire le parole in maniera decente
                matched_elements.append((nlp.vocab[matches[0][0]].text, doc[match_words[2]:match_words[0]][:2]))
            else:
                matched_elements.append((nlp.vocab[matches[0][0]].text, doc[match_words[0]:match_words[1]+1][1:]))#? doc[match_words[0] : match_words[1]+1] se non metto il +1 si mangia l'ultima parola ??

    return matched_elements #*matched element sarà una lista di tuple del tipo: ("nome_pattern", "parte di frase riconosciuta nel patter")




#TODO:aggiungere pattern per una risposta con soli ingredienti (Es. "Crisopa Fly", Es2. "Crisopa fly and Mazzei's moustache")
pattern1 = [
    {"RIGHT_ID": "attr",
     "RIGHT_ATTRS": {"LEMMA" : {"IN" : ["be", "use", "need", "have"]}}
    },
    {"LEFT_ID": "attr",
     "REL_OP": ">",
     "RIGHT_ID": "ingredient",
     "RIGHT_ATTRS": {"DEP": "attr"}
    }  
]
#? Sembra funzionante su passivo
passive_pattern = [
    {"RIGHT_ID": "passive",
     "RIGHT_ATTRS": {"LEMMA" : {"IN" : ["use", "need"]}}
    },
    {
     "LEFT_ID": "passive",
     "REL_OP": ">",
     "RIGHT_ID": "ingredient1",
     "RIGHT_ATTRS": {"DEP": "nsubjpass"}   
    },
    {
     "LEFT_ID": "ingredient1",
     "REL_OP": ">",
     "RIGHT_ID": "ingredient2",
     "RIGHT_ATTRS": {"DEP": {"IN": ["compound", "amod"]}}     
    }
]
#!? Abbozzato, funziona per la frase con contains, ma probabilmente si può generalizzare
pattern2 = [
    {"RIGHT_ID": "contains",
     "RIGHT_ATTRS": {"LEMMA" : {"IN" : ["contain"]}}
    },
    {
     "LEFT_ID": "contains",
     "REL_OP": ">",
     "RIGHT_ID": "ingredient_1",
     "RIGHT_ATTRS": {"DEP": "ccomp"}   
    },
    {"LEFT_ID": "contains",
     "REL_OP": ">",
     "RIGHT_ID": "ingredient_2",
     "RIGHT_ATTRS": {"DEP": "dobj"}
    }
]

answer1 = "the answer is Crisopa Fly..." #pattern 1 OK
answer2 = "the potion contains Crisopa fly" #pattern 3 OK
answer3 = "The first ingredient of the potion is the Crisopa fly" #pattern 1 OK
answer4 = "Crisopa fly is used in the potion" #pattern 2 OK
answer5 = "Crisopa Fly is needed in the potion" #pattern 2 OK
answer6 = "I think that Crisopa Fly is needed in the potion" #pattern 2 OK

start2 = time.time()
print(get_matched_patterns_from_dependency("aux_pattern", pattern1, answer1)) 
print(get_matched_patterns_from_dependency("aux_pattern", pattern2, answer2))
print(get_matched_patterns_from_dependency("aux_pattern", pattern1, answer3))
print(get_matched_patterns_from_dependency("aux_pattern", passive_pattern, answer4))
print(get_matched_patterns_from_dependency("aux_pattern", passive_pattern, answer5))
print(get_matched_patterns_from_dependency("aux_pattern", passive_pattern, answer6))
end2 = time.time()



print(f"metodo 2 ci mette {end2 - start2} secondi :)")


'''
#STEMMER ITALIANO
ps = SnowballStemmer('italian')
example_words = ["bambino","bambina","mosca","mosche", "Crisopa","crisopa", "crica", "criche"]

for w in example_words:
    print(ps.stem(w))

'''