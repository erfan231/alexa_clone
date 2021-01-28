import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id) # 0 is male 1 is female

def talk(command):
    engine.say(command)
    engine.runAndWait()

def main():
    try:
        with sr.Microphone() as source_audio:
            print("Listening...")
            voice = listener.listen(source_audio)
            command = listener.recognize_google(voice)
            command = command.lower()
            if "siri" in command:
                command = command.replace("siri", "")
                talk(command)
                print(command)
            elif "play" in command:
                command = command.replace("play", "playing")
                pywhatkit.playonyt(command)

            elif "time" in command:
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                print(current_time)
                talk("the time is {}".format(current_time))

            elif "info" in command:
                person = command[::1]
                print(person)
                info = wikipedia.summary(person, 1)
                talk(info)
            elif "information" in command:
                person = command[::1]
                print(person)
                info = wikipedia.summary(person, 5)
                talk(info)
            elif "joke" in command:
                talk(pyjokes.get_joke())

            else:
                talk("repeat...")
    except:
        talk("Did not understand... try again..")


def run_alexa():
    while True:
        main()


run_alexa()
        