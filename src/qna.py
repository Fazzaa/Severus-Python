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

# frase di inizio
def greetings():
    subject = nlg_factory.createNounPhrase(pick_random(GREETINGS))
    sentence = nlg_factory.createClause(subject)

    verb = nlg_factory.createVerbPhrase("be")
    subj = nlg_factory.createNounPhrase("name")
    subj.addPreModifier("your")
    sentence2 = nlg_factory.createClause(subj, verb)
    sentence2.setFeature(nlg.Feature.INTERROGATIVE_TYPE, nlg.InterrogativeType.WHAT_OBJECT)
    
    output = realiser.realiseSentence(sentence)
    output = f"{output} {realiser.realiseSentence(sentence2)}"
    return output

def start_interview(frame):
    s1 = nlg_factory.createSentence(f"Well Mr. {frame.get_student_name()}")

    verb = nlg_factory.createVerbPhrase("start")
    verb.setFeature(nlg.Feature.PERSON, nlg.Person.SECOND)
    verb.addPreModifier("Let's")
    obj = nlg_factory.createNounPhrase("interview")
    obj.addPreModifier("the")
    s2 = nlg_factory.createClause(verb, obj)

    output = realiser.realiseSentence(s1)
    output = f"{output} {realiser.realiseSentence(s2)}"
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

# frase del tipo: "Which ingredients are in Polyjuice potion ingredient's list?"
def ask_ingredients_be_0(frame):
    verb = nlg_factory.createVerbPhrase("be")
    verb.addPreModifier("Which")
    subject = nlg_factory.createNounPhrase("ingredient")
    subject.setPlural(True)
    object = nlg_factory.createNounPhrase("list")
    object.addPreModifier("in " + f"{frame.get_potion_name()}" +  " ingredient's")
    sentence = nlg_factory.createClause(subject, verb, object)
    sentence.setFeature(nlg.Feature.INTERROGATIVE_TYPE, nlg.InterrogativeType.YES_NO)
    output = realiser.realiseSentence(sentence)
    return output

# frase del tipo: "What does Polyjuice potion contain?"
def ask_ingredient_contain_0(frame):
    verb = nlg_factory.createVerbPhrase("contain")
    verb.setFeature(nlg.Feature.PERSON, nlg.Person.THIRD)
    subject = nlg_factory.createNounPhrase(f"{frame.get_potion_name()}")
    sentence = nlg_factory.createClause(subject, verb)
    sentence.setFeature(nlg.Feature.INTERROGATIVE_TYPE, nlg.InterrogativeType.WHAT_OBJECT)
    output = realiser.realiseSentence(sentence)
    return output

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

# frase del tipo: "What does Polyjuice potion not contain at all?"
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

def bad_response(frame, ingredient):
    if ingredient == "No Match":
        if frame.get_mood() == 2:    
            subj = nlg_factory.createNounPhrase("you")
            verb = nlg_factory.createVerbPhrase("want")
            verb.addPostModifier(f"me as an enemy, {frame.get_student_name()}")
            sentence = nlg_factory.createClause(subj, verb)
            sentence.setNegated(True)
        elif frame.get_mood() == 1:
            verb = nlg_factory.createVerbPhrase("waste")
            dobj = nlg_factory.createNounPhrase("time")
            dobj.addPreModifier("my")
            verb.setNegated(True)
            verb.setFeature(nlg.Feature.PERSON, nlg.Person.SECOND)
            sentence = nlg_factory.createClause(verb, dobj)
        else:
            verb =  nlg_factory.createVerbPhrase("try")
            verb.setFeature(nlg.Feature.PERSON, nlg.Person.SECOND)
            verb.addPostModifier("again")
            sentence = nlg_factory.createClause(verb)
    else:
        if frame.get_mood() == 2:
            subj = nlg_factory.createNounPhrase("you")
            verb = nlg_factory.createVerbPhrase("be")   
            obj = nlg_factory.createNounPhrase("stupid")
            obj.addPreModifier("so")   
            sentence = nlg_factory.createClause(subj, verb, obj)
            sentence.setFeature(nlg.Feature.INTERROGATIVE_TYPE, nlg.InterrogativeType.HOW)
        elif frame.get_mood() == 1:
            verb = nlg_factory.createVerbPhrase("be")
            subj = nlg_factory.createNounPhrase("That")
            obj = nlg_factory.createNounPhrase("wrong")
            obj.addPreModifier("totally")
            sentence = nlg_factory.createClause(subj, verb, obj)
        else:
            verb = nlg_factory.createVerbPhrase("be")
            subj = nlg_factory.createNounPhrase("That")
            obj = nlg_factory.createNounPhrase("ingredient")
            obj.addPreModifier("the correct")
            sentence = nlg_factory.createClause(subj, verb, obj)
            sentence.setNegated(True)

    output = realiser.realiseSentence(sentence)
    return output

def good_response(frame, ingredient):
    if frame.get_mood() == 2:    
        return "decent"
    elif frame.get_mood() == 1:
        return f"ok, {ingredient} it is correct"
    else:
        return "great!"


def valutation(frame, vote):
    verb = nlg_factory.createVerbPhrase("go")
    verb.setFeature(nlg.Feature.TENSE, nlg.Tense.PAST)
    subj = nlg_factory.createNounPhrase("interview")
    subj.addPreModifier(f"Well {frame.get_student_name()},")
    subj.addPreModifier("the")
    if vote < 18:
        obj = nlg_factory.createNounPhrase("bad")
        if vote == 0:
            obj.addPreModifier("very")
    elif vote >= 18 and vote <= 25:
        obj = nlg_factory.createNounPhrase("well")
    else:
        obj = nlg_factory.createNounPhrase("well")
        obj.addPreModifier("very")
    sentence_1 = nlg_factory.createClause(subj, verb, obj)
    output = realiser.realiseSentence(sentence_1)
    return output


