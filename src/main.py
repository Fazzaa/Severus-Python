import random
from potion import Potion
from frame import Frame
import spacy
from nltk import Tree

#funzione che restituisce una frase randomica da una lista di frasi
def pick_random_start(phrases_list):
    return random.choice(phrases_list)

'''da spostare'''



nlp = spacy.load('it_core_news_sm')

doc = nlp("Nella pozione polisucco sono presenti i sassi") 



def to_nltk_tree(node):
    if node.n_lefts + node.n_rights > 0:
        return Tree(node.orth_, [to_nltk_tree(child) for child in node.children])
    else:
        return node.orth_


#for token in doc:
#    print(token.text, token.pos_, token.dep_)

for sent in doc.sents:
    t = to_nltk_tree(sent.root)

print(t)


[to_nltk_tree(sent.root).pretty_print() for sent in doc.sents]
