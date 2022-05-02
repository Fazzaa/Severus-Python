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
    
    vote = get_vote(f)
    print(valutation(f, vote))

#? SPEECH RECOGNITION ON
else:
    print(greetings())
    name = speech_recognition()
    find_pattern_name(f, pattern_name, name)
    print(start_interview(f))

    while not f.full_frame() and f.get_chances() > 0:
        answer = speech_recognition()
        result = test_patterns(answer)
        
        if f.check_response(result):
            print(good_response())
        else:
            print(bad_response())
            f.dec_chances()
        
    vote = get_vote(f)
    print(valutation(f, vote))