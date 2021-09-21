import speech_recognition as sr
import pyttsx3
import pywhatkit

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[7].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_request():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'slave' in command:
                command = command.replace('slave', '')
                print(command)

    except:
        pass
    return command


def running_slave():
    #engine.say('Hello Master, what can i do for you?')
    command = take_request()
    print(command)
    if 'play' in command:V
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)


running_slave()