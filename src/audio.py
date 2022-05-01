import speech_recognition as sr

def speech_recognition():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio_text = recognizer.listen(source)
        try:
            print("Text: "+recognizer.recognize_google(audio_text))
        except:
            print("Sorry, I did not get that")

speech_recognition()