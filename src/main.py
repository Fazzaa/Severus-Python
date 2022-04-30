from frame import Frame
from dialogmanager import *
from patterns import *
from qna import ask_ingredients_be, greetings, start_interview

f = Frame()

name = input(greetings())
find_pattern_name(f, pattern_name, name)
print(start_interview(f))
print(f.get_mood())
print(f.get_chances())


while (len(f.get_student_ingredients()) < f.get_ingredients_number()) and f.get_chances() > 0:
    print(f.get_chances())
    answer = input(ask_ingredients_be(f))
    if f.check_response(test_patterns(answer)):
        print("Buono")
    else:
        print("Male")
        f.dec_chances()
        print(test_patterns(answer))
    
if f.get_chances() == 0:
    print("Figlio di puttana studia")
else:
    print("Sei l'orgoglio di Mazzei")
