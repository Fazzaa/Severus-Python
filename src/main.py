from frame import Frame
from dialogmanager import *
from patterns import *
from qna import ask_ingredients_be, greetings, start_interview

f = Frame()

name = input(greetings())
find_pattern_name(f, pattern_name, name)
print(start_interview(f))
print(ask_ingredients_be(f))

