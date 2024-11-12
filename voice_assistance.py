import pyttsx3

myName = 'Dash the voice'

engine = pyttsx3.init(sapi5)
voice = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.RunAndWait()

speak("HELLO THERE!")