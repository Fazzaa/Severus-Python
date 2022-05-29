from frame import Frame
from dialogmanager import *
from patterns import *
from qna import *
from audio import *

# Genero il frame che corrisponde ad una interrogazione
f = Frame()

f.set_mood(0);
print(f.get_mood())

speech = "0"
#* Scommenta per abilitare audio
# speech = input("Do you want to use the vocal interface? (y=1/n=0)")

# Controllo per modalità audio
if speech == "0":
    # Salva il nome del lo studente
    name = input(greetings())
    # Cerca il nome nella frase
    find_pattern_name(f, pattern_name, name)
    # Stampa frase inizio interrogazione
    print(start_interview(f))
    # Stampo le chance rimaste
    print(f"You have {f.get_chances()} chances")
    # Chiede il primo ingrediente
    answer = input(ask_ingredients(f))
    
    # Cicla fino a quando non sono stati detti tutti gli ingredienti o sono state esaurite le chance
    while not f.full_frame() and f.get_chances() > 0:
        
        # Estrae l'ingrediente dalla frase
        result = test_patterns(answer)
        
        # Controlla se l'ingrediente è corretto
        if f.check_response(result):
            # Entra solo si sono detti tutti gli ingredienti
            if not f.full_frame():
                # Se manca un solo ingrediente da inserire risponde così
                if f.remaining_ingredients() == 1:
                    answer = input(last_ingredient())                
                # Se ha inserito un solo ingrediente rispond così
                elif len(result) == 1: 
                    answer = input(ask_besides_ingredient(result[0]))
                else:
                    print(good_response(f))
                    answer = input(ask_ingredients(f))     
        else:
            print(bad_response(f))
            f.dec_chances()
            if f.get_chances() > 0:
                answer = input(ask_ingredients(f))
    
    vote = get_vote(f)
    print(valutation(f, vote))

#? SPEECH RECOGNITION ON
else:
    text = greetings()
    text_to_speech(text)
    name = speech_recognition()
    find_pattern_name(f, pattern_name, name)
    text = start_interview(f)
    text_to_speech(text)

    while not f.full_frame() and f.get_chances() > 0:
        text_to_speech(ask_ingredients(f))

        answer = speech_recognition()
        result = test_patterns(answer)
        
        if f.check_response(result):
            text = good_response(f)
            text_to_speech(text)
        else:
            text = bad_response(f)
            text_to_speech(text)
            f.dec_chances()
        
    vote = get_vote(f)
    text = valutation(f, vote)
    text_to_speech(text)