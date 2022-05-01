import speech_recognition as sr

def speech_recognition():
    result = ""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("...\n")
        audio_text = recognizer.listen(source)
        try:
            result = recognizer.recognize_google(audio_text)
            print(result)
        except:
            print("\n")
    return result
#speech_recognition()