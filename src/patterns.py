pattern = [
    {"DEP" : "ROOT"},
    {"IS_ALPHA" : True, "OP": "+"}
]

################DEP PARSER#####################
#? se non c'è un match con pattern_name prende tutta la stringa come nome utente, si assume che la stringa contiene tutto il nome
pattern_name = [
    {"RIGHT_ID": "attr",
    "RIGHT_ATTRS": {"LEMMA": {"IN": ["be"]}}
    },
    {"LEFT_ID": "attr",
    "REL_OP": ">",
    "RIGHT_ID": "name",
    "RIGHT_ATTRS": {"DEP": "attr"}
    }
]

pattern_aux = [
    {"RIGHT_ID": "attr",
    "RIGHT_ATTRS": {"LEMMA" : {"IN" : ["be", "use", "need", "have"]}}
    },
    {"LEFT_ID": "attr",
    "REL_OP": ">",
    "RIGHT_ID": "ingredient",
    "RIGHT_ATTRS": {"DEP": "attr"}
    },
    {"LEFT_ID": "ingredient",
    "REL_OP": ">",
    "RIGHT_ID": "ingredient_2",
    "RIGHT_ATTRS": {"DEP": {"IN" : ["compound"]}}
    }
]

#? Abbozzato, funziona per la frase con contains, ma probabilmente si può generalizzare
pattern_verb = [
    {"RIGHT_ID": "contains",
    "RIGHT_ATTRS": {"LEMMA" : {"IN" : ["contain"]}}
    },
    {
    "LEFT_ID": "contains",
    "REL_OP": ">",
    "RIGHT_ID": "ingredient_1",
    "RIGHT_ATTRS": {"DEP": {"IN" : ["dobj","ccomp"]}}   
    },
    {"LEFT_ID": "contains",
    "REL_OP": ">",
    "RIGHT_ID": "ingredient_2",
    "RIGHT_ATTRS": {"DEP": {"IN" : ["dobj","compound"]}}
    }
]
    

#? Sembra funzionante su passivo
passive_pattern_common = [
    {"RIGHT_ID": "passive",
    "RIGHT_ATTRS": {"LEMMA" : {"IN" : ["use", "need"]}}
    },
    {
    "LEFT_ID": "passive",
    "REL_OP": ">",
    "RIGHT_ID": "ingredient1",
    "RIGHT_ATTRS": {"DEP": {"IN": ["nsubjpass", "csubjpass"]}}   
    },
    {
    "LEFT_ID": "ingredient1",
    "REL_OP": ">",
    "RIGHT_ID": "ingredient2",
    "RIGHT_ATTRS": {"DEP": {"IN": ["compound", "amod","poss", "dobj"]}}     
    }
]
passive_pattern_propn = [
    {"RIGHT_ID": "passive",
    "RIGHT_ATTRS": {"LEMMA" : {"IN" : ["use", "need"]}}
    },
    {
    "LEFT_ID": "passive",
    "REL_OP": ">",
    "RIGHT_ID": "ingredient1",
    "RIGHT_ATTRS": {"DEP": {"IN": ["nsubjpass", "csubjpass"]}}   
    },
    {
    "LEFT_ID": "ingredient1",
    "REL_OP": ">",
    "RIGHT_ID": "ingredient2",
    "RIGHT_ATTRS": {"DEP": {"IN": ["compound", "amod","poss", "dobj"]}}     
    },
    {
    "LEFT_ID": "ingredient2",
    "REL_OP": ">",
    "RIGHT_ID": "ingredient3",
    "RIGHT_ATTRS": {"DEP": {"IN": ["compound", "amod","poss", "dobj"]}}     
    }
]

#TODO:aggiungere pattern per una risposta con soli ingredienti (Es. "Crisopa Fly", Es2. "Crisopa fly and Mazzei's moustache")
