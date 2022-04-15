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





'''
#STEMMER ITALIANO
ps = SnowballStemmer('italian')
example_words = ["bambino","bambina","mosca","mosche", "Crisopa","crisopa", "crica", "criche"]

for w in example_words:
    print(ps.stem(w))

'''

'''
PROBABILMENTE INUTILE
def to_nltk_tree(node):
    if node.n_lefts + node.n_rights > 0:
        return Tree(node.orth_, [to_nltk_tree(child) for child in node.children])
    else:
        return node.orth_

def print_token(sentence):
    for token in sentence:
        print(token.text, token.pos_, token.dep_)

def to_tree(sentence):
    for sent in sentence.sents:
        t = to_nltk_tree(sent.root)
    return t

def pretty_print_tree(sentence):
    [to_nltk_tree(sent.root).pretty_print() for sent in sentence.sents]

def profundity_research(tree):
    if isinstance(tree, Tree):
        print(tree.label())
        for child in tree:
            profundity_research(child)
    else:
        print(tree)
    
'''