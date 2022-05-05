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
            print(good_response(f))
        else:
            print(bad_response(f))
            f.dec_chances()
    
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
            text = good_response(f, result)
            text_to_speech(text)
        else:
            text = bad_response(f)
            text_to_speech(text)
            f.dec_chances()
        
    vote = get_vote(f)
    text = valutation(f, vote)
    text_to_speech(text)