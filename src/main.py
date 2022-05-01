from frame import Frame
from dialogmanager import *
from patterns import *
from qna import *
<<<<<<< HEAD
from audio import *

=======
>>>>>>> 760ad7b774206a14294055762845bad6c1294cda

f = Frame()

<<<<<<< HEAD
    while (len(f.get_student_ingredients()) < f.get_ingredients_number()) and f.get_chances() > 0:
        answer = input(ask_ingredients_be(f))
        result = test_patterns(answer)
        if result != None:
            if f.check_response(result):
                print("Buono")
            else:
                bad_response()
                f.dec_chances()
                print(test_patterns(answer))
        else:
            print("I don't understand you")
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
        print(ask_ingredients_be(f))
        answer = speech_recognition()
        result = test_patterns(answer)
        if result != None:
            if f.check_response(result):
                print("Buono")
            else:
                bad_response()
                f.dec_chances()
                print(test_patterns(answer))
        else:
            print("I don't understand you!")
            f.dec_chances()
        
    if f.get_chances() == 0:
        print("Figlio di puttana studia")
    else:
        print("Sei l'orgoglio di Mazzei")
=======
name = input(greetings())
find_pattern_name(f, pattern_name, name)
print(start_interview(f))
print(f.get_mood())
print(f.get_chances())


while (len(f.get_student_ingredients()) < f.get_ingredients_number()) and f.get_chances() > 0:
    answer = input(ask_ingredients_be(f))
    result = test_patterns(answer)
    if result != None:
        if f.check_response(result):
            if not f.full_frame():
                good_response()
        else:
            bad_response()
            f.dec_chances()
    else:
        print("I don't understand you!")
        
if f.get_chances() == 0:
    print("Figlio di puttana studia")
else:
    print("Sei l'orgoglio di Mazzei")

print(similar("Crisopa Flies","Crisopa Fly"))
>>>>>>> 760ad7b774206a14294055762845bad6c1294cda
