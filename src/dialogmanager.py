import random
import spacy
from patterns import *
from spacy.matcher import Matcher
from spacy.matcher import DependencyMatcher
from difflib import SequenceMatcher


patterns_name = ["passive_pattern_common","passive_pattern_propn", "pattern_verb","pattern_aux", "pattern_verb_2"]
patterns = [passive_pattern_common, passive_pattern_propn, pattern_verb, pattern_aux, pattern_verb_2]

nlp = spacy.load('en_core_web_sm')
        
def pick_random(phrases_list):
    return random.choice(phrases_list)

# TODO: riuscire a passare in input una lista di patter (?) e magari una lista di nomi di pattern associati 
# TODO: (in modo da riuscire a capire quale pattern ha fatto match e avere il nome del pattern)

def get_matched_patterns_from_dependency(name_pattern, pattern, text):
    matched_elements = [] 
    matcher = DependencyMatcher(nlp.vocab)
    matcher.add(name_pattern, [pattern])
    doc = nlp(text)
    matches = matcher(doc)
    matches.sort(key = lambda x : x[1])
    for match in matches:
        match_words = sorted(match[1])
        print(match_words)
        if name_pattern == "passive_pattern_propn" or name_pattern == "passive_pattern_common":
            matched_elements.append(doc[match_words[0]:match_words[len(match_words)-1]][:-1])
        elif name_pattern == "pattern_verb" or name_pattern == "pattern_aux" or name_pattern == "pattern_verb_2":
            matched_elements.append(doc[match_words[0]+1:match_words[len(match_words)-1]+1])

    if len(matched_elements) == 0:
        return ["No Match"]
    return matched_elements[0].text

def find_pattern_name(frame, pattern, text):
    matcher = DependencyMatcher(nlp.vocab)
    matcher.add("name_pattern", [pattern])
    doc = nlp(text)
    matches = matcher(doc)
    matches.sort(key = lambda x : x[1])
    if len(matches)==0:
        frame.set_student_name(text)
    else:
        name = doc[matches[0][1][0]+1:matches[0][1][1]+1]
        frame.set_student_name(name.text)

def test_patterns(text):
    i = 0
    while i < len(patterns):
        result = get_matched_patterns_from_dependency(patterns_name[i], patterns[i], text)
        if result[0] != "No Match":
            result = result.split(",")
            return result
        i += 1
    text = text.split(',')
    return text

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def get_vote(frame):
    good_answer = round((len(frame.get_student_ingredients()) / frame.get_ingredients_number())*30, 0)
    if frame.full_frame():
        if frame.get_chances() < frame.get_initial_chances():
            return good_answer - frame.get_mood()
    else:
        if frame.get_mood() == 0 and good_answer >= 16:
            return 18
    
    return good_answer


    
