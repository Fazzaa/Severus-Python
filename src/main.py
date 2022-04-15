import random
from potion import Potion
from frame import Frame
import spacy
from nltk import Tree
from spacy.symbols import cop
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
asw = find_ing_by_copula(doc)
f.check_response(asw)   
print(f"Ingredienti giusti: {f.get_student_ingredients()}")


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