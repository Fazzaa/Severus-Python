import speech_recognition as sr
import gtts
from playsound import playsound


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

def text_to_speech(text):
    tts = gtts.gTTS(text, lang="it")
    tts.save("audio.mp3")
    playsound("audio.mp3")
