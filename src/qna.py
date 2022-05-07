# Piton question and answer
import simplenlg as nlg
from dialogmanager import *
from constants import *
from frame import Frame


lexicon = nlg.Lexicon.getDefaultLexicon()
nlg_factory = nlg.NLGFactory(lexicon)
realiser = nlg.Realiser(lexicon) 

# L'idea è che il dialogue manager scelga quali di queste funzioni usare 
# a seconda delle risposte dell'utente

#* OK
def greetings():
    s_1 = nlg_factory.createClause(pick_random(GREETINGS))

    verb = nlg_factory.createVerbPhrase("be")
    subj = nlg_factory.createNounPhrase("your", "name")
    s_2 = nlg_factory.createClause(subj, verb)
    s_2.setFeature(nlg.Feature.INTERROGATIVE_TYPE, nlg.InterrogativeType.WHAT_OBJECT)
    
    coord = nlg_factory.createCoordinatedPhrase()
    coord.setConjunction(",")
    coord.addCoordinate(s_1)
    coord.addCoordinate(s_2)

    output = realiser.realiseSentence(coord)
    return output

#* OK
def start_interview(frame):
    s_1 = nlg_factory.createClause(f"Well {frame.get_student_name()}")

    subj_2 = nlg_factory.createNounPhrase("we")
    verb_2 = nlg_factory.createVerbPhrase("start")
    verb_2.setFeature(nlg.Feature.PERSON, nlg.Person.SECOND)
    verb_2.setFeature(nlg.Feature.MODAL, "can")
    obj_2 = nlg_factory.createNounPhrase("the", "interview")
    s_2 = nlg_factory.createClause(subj_2, verb_2, obj_2)

    coord = nlg_factory.createCoordinatedPhrase()
    coord.setConjunction(",")
    coord.addCoordinate(s_1)
    coord.addCoordinate(s_2)

    output = realiser.realiseSentence(coord)
    return output

def ask_ingredients(f):
    if f.get_mood() == 0:
        return ask_ingredient_contain_0(f)
    elif f.get_mood() == 1:
        return ask_ingredients_be_0(f)
    elif f.get_mood() == 2:
        return ask_ingredient_contain_0(f)
    else:
        pass
        #potter_mode()
        
#######QUESTIONS########

#! non controllata
# frase del tipo: "Which ingredients are in Polyjuice potion ingredient's list?"
def ask_ingredients_be_0(frame):
    n = pick_random([1,2])
    if n == 1:
        verb = nlg_factory.createVerbPhrase("be")
    if n == 2:
        verb = nlg_factory.createVerbPhrase("be")
        verb.setFeature(nlg.Feature.MODAL, "must")
    subject = nlg_factory.createNounPhrase("ingredient")
    subject.setPlural(True)
    object = nlg_factory.createNounPhrase("list")
    object.addPreModifier("in " + f"{frame.get_potion_name()}" +  " ingredient's")
    
    sentence = nlg_factory.createClause(subject, verb, object)
    sentence.setFeature(nlg.Feature.INTERROGATIVE_TYPE, nlg.InterrogativeType.WHAT_SUBJECT)
    
    output = realiser.realiseSentence(sentence)
    return output

#! non controllata
# frase del tipo: "What does Polyjuice potion contain?"
def ask_ingredient_contain_0(frame):
    verb = nlg_factory.createVerbPhrase("contain")
    verb.setFeature(nlg.Feature.PERSON, nlg.Person.THIRD)
    subject = nlg_factory.createNounPhrase(f"{frame.get_potion_name()}")
    sentence = nlg_factory.createClause(subject, verb)
    sentence.setFeature(nlg.Feature.INTERROGATIVE_TYPE, nlg.InterrogativeType.WHAT_OBJECT)
    output = realiser.realiseSentence(sentence)
    return output

#! non controllata
# frase del tipo: "What does Polyjuice potion else contain?"
def ask_ingredient_contain_else(potion):
    verb = nlg_factory.createVerbPhrase("contain")
    verb.setFeature(nlg.Feature.PERSON, nlg.Person.THIRD)
    verb.addModifier("else")
    subject = nlg_factory.createNounPhrase(f"{potion}")
    sentence = nlg_factory.createClause(subject, verb)
    sentence.setFeature(nlg.Feature.INTERROGATIVE_TYPE, nlg.InterrogativeType.WHAT_OBJECT)
    output = realiser.realiseSentence(sentence)
    return output


#! non controllata
# frase del tipo: "Which ingredient between Crisopa fly and Murtlap's tentacle is in Polyjuice potion ingredient's list?"
def ask_ingredient_between(potion, ingredient1, ingredient2):
    verb = nlg_factory.createVerbPhrase("be")
    verb.addPreModifier("Which")
    subject = nlg_factory.createNounPhrase("ingredient")
    subject.addComplement("between " + f"{ingredient1}" + " and " + f"{ingredient2}")
    object = nlg_factory.createNounPhrase("list")
    object.addPreModifier("in " + f"{potion}" +  " ingredient's")
    sentence = nlg_factory.createClause(subject, verb, object)
    sentence.setFeature(nlg.Feature.INTERROGATIVE_TYPE, nlg.InterrogativeType.YES_NO)
    output = realiser.realiseSentence(sentence)
    return output

#! non controllata
def ask_not_contain(potion):
    sentence = nlg_factory.createClause()
    sentence.setSubject(f"{potion}")
    sentence.setVerb("contain")
    sentence.setObject("Crisopa Fly")
    sentence.setNegated(True)
    sentence.setFeature(nlg.Feature.TENSE, nlg.Tense.PRESENT)
    sentence.setFeature(nlg.Feature.INTERROGATIVE_TYPE, nlg.InterrogativeType.WHAT_OBJECT)
    sentence.addComplement("at all")
    output = realiser.realiseSentence(sentence)
    return output

########ANSWERS########
#?DA REVISIONARE ALCUNE FRASI
def bad_response(frame):
    n = pick_random([1,2])
    if frame.get_mood() == 2:
        subj = nlg_factory.createNounPhrase("you")
        if n == 1:
            verb = nlg_factory.createVerbPhrase("want")
            verb.addPostModifier(f"me as an enemy, {frame.get_student_name()}")
            sentence = nlg_factory.createClause(subj, verb)
            sentence.setNegated(True)
        else:
            verb = nlg_factory.createVerbPhrase("be")   
            verb.setFeature(nlg.Feature.MODAL, "can")
            obj = nlg_factory.createNounPhrase("so", "stupid")
            sentence = nlg_factory.createClause(subj, verb, obj)
            sentence.setFeature(nlg.Feature.INTERROGATIVE_TYPE, nlg.InterrogativeType.HOW)
    elif frame.get_mood() == 1:
        if n == 1:
            verb = nlg_factory.createVerbPhrase("waste")
            verb.setNegated(True)
            verb.setFeature(nlg.Feature.PERSON, nlg.Person.SECOND)
            dobj = nlg_factory.createNounPhrase("my", "time")
            
            sentence = nlg_factory.createClause(verb, dobj)
        else:
            subj = nlg_factory.createNounPhrase("That")
            verb = nlg_factory.createVerbPhrase("be")
            obj = nlg_factory.createNounPhrase("totally", "wrong")

            sentence = nlg_factory.createClause(subj, verb, obj)
    else:
        if n == 1:
            verb =  nlg_factory.createVerbPhrase("try")
            verb.setFeature(nlg.Feature.PERSON, nlg.Person.SECOND)
            verb.addPostModifier("again")
            
            sentence = nlg_factory.createClause(verb)
        else: 
            verb = nlg_factory.createVerbPhrase("be")
            verb.setNegated(True)
            subj = nlg_factory.createNounPhrase("That")
            obj = nlg_factory.createNounPhrase("the correct", "ingredient")

            sentence = nlg_factory.createClause(subj, verb, obj)
            
    output = realiser.realiseSentence(sentence)
    return output

#*CREDO OK
def good_response(frame):
    if frame.get_mood() == 2:    
        verb_1 = nlg_factory.createVerbPhrase("be")
        subj_1 = nlg_factory.createNounPhrase("That")
        obj_1 = nlg_factory.createNounPhrase("slightly", "sufficient")
        s_1 = nlg_factory.createClause(subj_1, verb_1, obj_1)

        verb_2 = nlg_factory.createVerbPhrase("go on")
        verb_2.setFeature(nlg.Feature.MODAL, "can")
        subj_2 = nlg_factory.createNounPhrase("you")
        s_2 = nlg_factory.createClause(subj_2, verb_2)

        coord = nlg_factory.createCoordinatedPhrase()
        coord.setConjunction(",")
        coord.addCoordinate(s_1)
        coord.addCoordinate(s_2)

        output = realiser.realiseSentence(coord)
        
    elif frame.get_mood() == 1:
        s_1 = nlg_factory.createClause("Ok")

        subj_2 = nlg_factory.createNounPhrase("it")
        verb_2 = nlg_factory.createVerbPhrase("be")
        obj_2 = nlg_factory.createNounPhrase("correct")
        s_2 = nlg_factory.createClause(subj_2, verb_2, obj_2)

        coord = nlg_factory.createCoordinatedPhrase()
        coord.setConjunction(",")
        coord.addCoordinate(s_1)
        coord.addCoordinate(s_2)

        output = realiser.realiseSentence(coord)
        
    else:
        verb = nlg_factory.createVerbPhrase("be")
        subj = nlg_factory.createNounPhrase("That")
        obj = nlg_factory.createNounPhrase("the correct", "ingredient")
        s_1 = nlg_factory.createClause(subj, verb, obj)

        output = realiser.realiseSentence(s_1)

    return output

def ask_besides_ingredient(ingredient):
    s_0 = nlg_factory.createClause("Ok")

    subj_2 = nlg_factory.createNounPhrase("it")
    verb_2 = nlg_factory.createVerbPhrase("be")
    obj_2 = nlg_factory.createNounPhrase("correct")
    s_2 = nlg_factory.createClause(subj_2, verb_2, obj_2)

    coord = nlg_factory.createCoordinatedPhrase()
    coord.setConjunction(",")
    coord.addCoordinate(s_0)
    coord.addCoordinate(s_2)
    subj = nlg_factory.createNounPhrase("the", "potion")
    verb = nlg_factory.createVerbPhrase("contain")
    obj = nlg_factory.createNounPhrase("ingredient")
    p_2 = nlg_factory.createNounPhrase(f"besides {ingredient}")
    s_1 = nlg_factory.createClause(subj, verb, obj)
    s_1.addPostModifier(p_2)
    s_1.setFeature(nlg.Feature.INTERROGATIVE_TYPE, nlg.InterrogativeType.WHAT_OBJECT)

    output = realiser.realiseSentence(coord) + " " + realiser.realiseSentence(s_1)
    return output


def last_ingredient():
    verb = nlg_factory.createVerbPhrase("be")
    subj = nlg_factory.createNounPhrase("That")
    obj = nlg_factory.createNounPhrase("the correct", "ingredient")
    s_1 = nlg_factory.createClause(subj, verb, obj)
    
    verb_2 = nlg_factory.createVerbPhrase("be")
    verb_2.setFeature(nlg.Feature.TENSE, nlg.Tense.PRESENT)
    subj_2 = nlg_factory.createNounPhrase("the last", "ingredient")
    s_2 = nlg_factory.createClause(subj_2, verb_2)
    s_2.setFeature(nlg.Feature.INTERROGATIVE_TYPE, nlg.InterrogativeType.WHAT_OBJECT)
    output = realiser.realiseSentence(s_1) + " " + realiser.realiseSentence(s_2)
    return output

#*OK
def valutation(frame, vote):
    s_1 = nlg_factory.createClause(f"Well {frame.get_student_name()}")

    verb_2 = nlg_factory.createVerbPhrase("go")
    verb_2.setFeature(nlg.Feature.TENSE, nlg.Tense.PAST)
    subj_2 = nlg_factory.createNounPhrase("the", "interview")
    
    if vote == "Troll":
        obj_2 = nlg_factory.createNounPhrase("very", "bad")
    if vote == "Poor" or vote == "Dreadful":
        obj_2 = nlg_factory.createNounPhrase("bad")
    elif vote == "Acceptable" or vote == "Exceeds Expectations":
        obj_2 = nlg_factory.createNounPhrase("well")
    else:
        obj_2 = nlg_factory.createNounPhrase("very", "well")

    s_2 = nlg_factory.createClause(subj_2, verb_2, obj_2)
    
    subj_3 = nlg_factory.createNounPhrase("your", "vote")
    verb_3 = nlg_factory.createVerbPhrase("be")
    obj_3 = nlg_factory.createNounPhrase(vote)
    s_3 = nlg_factory.createClause(subj_3, verb_3, obj_3)

    coord = nlg_factory.createCoordinatedPhrase()
    coord.addCoordinate(s_1)
    coord.addCoordinate(s_2)
    coord.addCoordinate(s_3)

    output = realiser.realiseSentence(coord)
    return output
