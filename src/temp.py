#TODO:aggiungere pattern per una risposta con soli ingredienti (Es. "Crisopa Fly", Es2. "Crisopa fly and Mazzei's moustache")
pattern1 = [
    {"RIGHT_ID": "attr",
    "RIGHT_ATTRS": {"LEMMA" : {"IN" : ["be", "use", "need", "have"]}}
    },
    {"LEFT_ID": "attr",
    "REL_OP": ">",
    "RIGHT_ID": "ingredient",
    "RIGHT_ATTRS": {"DEP": "attr"}
    }  
]
#? Sembra funzionante su passivo
passive_pattern = [
    {"RIGHT_ID": "passive",
    "RIGHT_ATTRS": {"LEMMA" : {"IN" : ["use", "need"]}}
    },
    {
    "LEFT_ID": "passive",
    "REL_OP": ">",
    "RIGHT_ID": "ingredient1",
    "RIGHT_ATTRS": {"DEP": "nsubjpass"}   
    },
    {
    "LEFT_ID": "ingredient1",
    "REL_OP": ">",
    "RIGHT_ID": "ingredient2",
    "RIGHT_ATTRS": {"DEP": {"IN": ["compound", "amod"]}}     
    }
]
#!? Abbozzato, funziona per la frase con contains, ma probabilmente si può generalizzare
pattern2 = [
    {"RIGHT_ID": "contains",
    "RIGHT_ATTRS": {"LEMMA" : {"IN" : ["contain"]}}
    },
    {
    "LEFT_ID": "contains",
    "REL_OP": ">",
    "RIGHT_ID": "ingredient_1",
    "RIGHT_ATTRS": {"DEP": "ccomp"}   
    },
    {"LEFT_ID": "contains",
    "REL_OP": ">",
    "RIGHT_ID": "ingredient_2",
    "RIGHT_ATTRS": {"DEP": "dobj"}
    }
]

answer1 = "the answer is Crisopa Fly..." #pattern 1 OK
answer2 = "the potion contains Crisopa fly" #pattern 3 OK
answer3 = "The first ingredient of the potion is the Crisopa fly" #pattern 1 OK
answer4 = "Crisopa fly is used in the potion" #pattern 2 OK
answer5 = "Crisopa Fly is needed in the potion" #pattern 2 OK
answer6 = "I think that Crisopa Fly is needed in the potion" #pattern 2 OK


'''
#STEMMER ITALIANO
ps = SnowballStemmer('italian')
example_words = ["bambino","bambina","mosca","mosche", "Crisopa","crisopa", "crica", "criche"]

for w in example_words:
    print(ps.stem(w))
if PATTERNS_NAME[i] not in freq:
    freq[PATTERNS_NAME[i]] = 1
else:
    freq[PATTERNS_NAME[i]] += 1

'''
