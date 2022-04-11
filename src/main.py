import random
from potion import Potion
from frame import Frame
import spacy
from nltk import Tree
from spacy import displacy

#funzione che restituisce una frase randomica da una lista di frasi
def pick_random_start(phrases_list):
    return random.choice(phrases_list)

'''da spostare'''



nlp = spacy.load('it_core_news_sm')

doc = nlp("Nella pozione polisucco sono presenti i sassi") 
displacy.serve(doc, style='dep')

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

t = to_tree(doc)
print(t)

pretty_print_tree(doc)
profundity_research(t)



