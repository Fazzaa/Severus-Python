import random
from potion import Potion
from frame import Frame

#funzione che restituisce una frase randomica da una lista di frasi
def pick_random_start(phrases_list):
    return random.choice(phrases_list)

'''da spostare'''
import spacy
from nltk import Tree


nlp = spacy.load('en_core_web_sm')

doc = nlp("The answer is Crisopa fly.") 

def to_nltk_tree(node):
    if node.n_lefts + node.n_rights > 0:
        return Tree(node.orth_, [to_nltk_tree(child) for child in node.children])
    else:
        return node.orth_


for token in doc:
    print(token.text, token.pos_, token.dep_)

[to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
