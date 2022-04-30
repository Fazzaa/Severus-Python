# Piton question and answer
import simplenlg as nlg
from dialogmanager import *
from constants import *
from frame import Frame


frame = Frame()
lexicon = nlg.Lexicon.getDefaultLexicon()
nlg_factory = nlg.NLGFactory(lexicon)
realiser = nlg.Realiser(lexicon) 

#! dubbio esistenziale, tutta sta libreria mi sembra inutile, si assemblano le frasi logicamente ma alla fine è come se le avessi scritte a mano
#! chiedere a Mazzei come va usata per email, per avere meno paranoie.
#! cosa cambia tra queste generate con questo bel criterio logico e quelle scritte banalmente tipo 
#! "Which ingredients contains f{potion}?" ??? 



#* idea per rendere il tutto meno statico, aggiungere funzioni random che cambiano le comppnenti delle frasi
#* tipo una lista di verbi tra cui scegliere al posto di "contains" ecc...

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


# frase del tipo: "Which ingredients are in Polyjuice potion ingredient's list?"
def ask_ingredients_be(potion):
    verb = nlg_factory.createVerbPhrase("be")
    verb.addPreModifier("Which")
    subject = nlg_factory.createNounPhrase("ingredient")
    subject.setPlural(True)
    object = nlg_factory.createNounPhrase("list")
    object.addPreModifier("in " + f"{potion}" +  " ingredient's")
    sentence = nlg_factory.createClause(subject, verb, object)
    sentence.setFeature(nlg.Feature.INTERROGATIVE_TYPE, nlg.InterrogativeType.YES_NO)
    output = realiser.realiseSentence(sentence)
    return output

# frase del tipo: "What does Polyjuice potion contain?"
def ask_ingredient_contain(potion):
    verb = nlg_factory.createVerbPhrase("contain")
    verb.setFeature(nlg.Feature.PERSON, nlg.Person.THIRD)
    subject = nlg_factory.createNounPhrase(f"{potion}")
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




# Test
'''
print(ask_ingredients_be("Polyjuice potion"))
print(ask_ingredient_contain("Polyjuice potion"))
print(ask_ingredient_contain_else("Polyjuice potion"))
print(ask_ingredient_between("Polyjuice potion", "Crisopa Fly", "Murtlap's tentacle"))
print(ask_not_contain("Polyjuice potion"))
print(greetings())
'''

print(start_interview(frame))