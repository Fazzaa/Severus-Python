from frame import Frame
from dialogmanager import *
from patterns import *
from qna import *
from audio import *


f = Frame()
speech = input("Do you want to use the vocal interface? (y=1/n=0)")

if speech == "0":
    name = input(greetings())
    find_pattern_name(f, pattern_name, name)
    print(start_interview(f))
    print(f"You have {f.get_chances()} chances")
    
    while not f.full_frame() and f.get_chances() > 0:
        answer = input(ask_ingredients(f))
        result = test_patterns(answer)
        
        if f.check_response(result):
            print(good_response(f, result))
        else:
            print(bad_response(f, result))
            f.dec_chances()
        
    if f.get_chances() == 0:
        print("Figlio di puttana studia")
    else:
        print("Sei l'orgoglio di Mazzei")

#? SPEECH RECOGNITION ON
else:
    print(greetings())
    name = speech_recognition()
    find_pattern_name(f, pattern_name, name)
    print(start_interview(f))
    print(f.get_mood())
    print(f.get_chances())

    while (len(f.get_student_ingredients()) < f.get_ingredients_number()) and f.get_chances() > 0:
        print(ask_ingredients(f))
        answer = speech_recognition()
        result = test_patterns(answer)
        
        if f.check_response(result):
            print("Buono")
        else:
            print(bad_response())
            f.dec_chances()
            print(test_patterns(answer))
        
    if f.get_chances() == 0:
        print("Figlio di puttana studia")
    else:
        print("Sei l'orgoglio di Mazzei")
