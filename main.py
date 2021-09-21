import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

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
            if 'jarvis' in command:
                command = command.replace('jarvis', '')
                print(command)

    except:
        pass
    return command


def running_slave():
    command = take_request()
    print(command)
    if 'play' in command:
        song = command.replace('play', '')
        talk('playing' + song)
        pywhatkit.playonyt(song)
    elif 'google' in command:
        search = command.replace('google', '')
        talk(search)
        pywhatkit.search(search)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%H:%M')
        talk('The current time is, ' + time)
    elif 'search for' in command:
        search = command.replace('search for', '')
        info = wikipedia.summary(search, 1)
        print(info)
        talk(info)
    elif 'gay' in command:
        talk('Why are you gay?')
        talk('You are gay!')
    elif 'joke' in command:
        joke = pyjokes.get_joke()
        talk(joke)
        print(joke)
    else:
        talk('Please repeat.')

while True:
    running_slave()
