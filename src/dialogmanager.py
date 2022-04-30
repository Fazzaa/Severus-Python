import random
import spacy
from spacy.matcher import Matcher
from spacy.matcher import DependencyMatcher

# HINT1: SE AUX È PRESENTE -> INGREDIENTE È COPULA DI AUX
# HINT2: SE VERB È PRESENTE -> INGREDIENTE NSUBJ DI VERB
# HINT3: SE NON È PRESENTE NE VERB NE AUX -> È TUTTO INGREDIENTE
# HINT4: Lavorare su risposta che ha solo ingredienti (senza verbi)
    
nlp = spacy.load('en_core_web_sm')
        
def pick_random(phrases_list):
    """Return a random element from a list."""
    return random.choice(phrases_list)

#* Alternativa con matcher per riconoscere il pattern:
#* matcher spacy http://spacy.pythonhumanities.com/02_02_matcher.html#
#* si utlizza la stessa funzione per riconoscere i vari pattern, si possono così
#* creare più pattern da usare a seconda della parola senza dover fare 50 funzioni

def get_matched_patterns(name_pattern, pattern, text):
    """Find the pattern in the text and return the matched elements"""
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
    

#TODO: implementare modo per togliere l'articolo dalla frase matchata, si può fare direttamente nel 
#TODO: frame nella funzione check_response così il match è più facile e si ottengono informazioni belle
    

#* Alternativa con dependency matcher per riconoscere il pattern
# TODO: DISCLAIMER: i nomi dei pattern e dei vari attributi sono opinabili, lo so. Sentitevi liberi di cambiarli.
# TODO: riuscire a passare in input una lista di patter (?) e magari una lista di nomi di pattern associati 
# TODO: (in modo da riuscire a capire quale pattern ha fatto match e avere il nome del pattern)

def get_matched_patterns_from_dependency(name_pattern, pattern, text):
    '''Recognizes the pattern passed as a parameter within a text using the spacy dependency matcher'''
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
    if len(matched_elements) == 0:
        return "No match"
    return matched_elements #*matched element sarà una lista di tuple del tipo: ("nome_pattern", "parte di frase riconosciuta nel patter")
