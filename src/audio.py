import speech_recognition as sr
import gtts
from playsound import playsound
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer


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
    tts = gtts.gTTS(text, lang="en")
    tts.save("audio.mp3")
    playsound("audio.mp3")



tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
sequence = ("Your father was a pig")
inputs = tokenizer.encode(sequence, return_tensors="pt")
outputs = model.generate(inputs, max_length=50, do_sample=True, temperature=0.8, top_k=50)
text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(text)

