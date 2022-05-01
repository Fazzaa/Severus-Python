from frame import Frame
from dialogmanager import *
from patterns import *
from qna import *

f = Frame()

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
            if f.full_frame():
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