import random
import spacy
from patterns import *
from spacy.matcher import DependencyMatcher
from difflib import SequenceMatcher

vote_dictionary = {0: "Troll",1: "Troll",2: "Troll",3: "Dreadful",4: "Dreadful",5: "Poor",6: "Acceptable",
                   7: "Acceptable",8: "Exceeds Expectations",9: "Exceeds Expectations",10: "Outstanding"}
patterns_name = ["passive_pattern_2","pattern_verb_5", "pattern_verb_4","passive_pattern_propn", "passive_pattern_common", "pattern_verb","pattern_aux", "pattern_verb_2","passive_pattern", "pattern_verb_3"]
patterns = [passive_pattern_2, pattern_verb_5, pattern_verb_4,passive_pattern_propn, passive_pattern_common, pattern_verb, pattern_aux, pattern_verb_2, passive_pattern, pattern_verb_3]

nlp = spacy.load('en_core_web_sm')
        
def pick_random(phrases_list):
    return random.choice(phrases_list)

def get_longest(match_list):
    l = ""
    for match in match_list:
        if len(match) > len(l):
            l = match
    return l



def get_matched_patterns_from_dependency(name_pattern, pattern, text):
    matched_elements = [] 
    matcher = DependencyMatcher(nlp.vocab)
    matcher.add(name_pattern, [pattern])
    doc = nlp(text.lower())
    matches = matcher(doc)
    matches.sort(key = lambda x : x[1])
    for match in matches:
        match_words = sorted(match[1])
        print(name_pattern)
        if name_pattern == "passive_pattern_propn" or name_pattern == "passive_pattern_common" or name_pattern == "passive_pattern" or name_pattern == "passive_pattern_2":
            matched_elements.append(doc[match_words[0]:match_words[len(match_words)-1]][:-1])
        elif name_pattern == "pattern_verb" or name_pattern == "pattern_aux" or name_pattern == "pattern_verb_2" or name_pattern == "pattern_verb_3" or name_pattern == "pattern_verb_4" or name_pattern == "pattern_verb_5":
            matched_elements.append(doc[match_words[0]+1:match_words[len(match_words)-1]+1])

    if len(matched_elements) == 0:
        return "No Match"
    
    result = get_longest(matched_elements)
    return result.text
    


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
        if result != "No Match":
            result = result.split(",")
            return result
        i += 1
    text = text.split(',')
    return text

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def get_vote(frame):
    n_vote = round((len(frame.get_student_ingredients()) / frame.get_ingredients_number())*10,0)
    if frame.full_frame():
        if frame.get_chances() < frame.get_initial_chances():
            n_vote = n_vote - frame.get_mood()
    else:
        if frame.get_mood() == 0 and n_vote >= 5:
            n_vote = 6
    
    return vote_dictionary[n_vote]

