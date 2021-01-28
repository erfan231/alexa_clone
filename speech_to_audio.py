import speech_recognition as sr

r = sr.Recognizer

#reading audio file as source
# listening the audio file and store in audio_text variable


with sr.AudioFile("speech.wav") as source:
    audio_text = r.listen(source)


    try:
        #using goolge speech recognition
        text = r.recognize_google(audio_text) #different lang = language= "fr=FR"
        print("Converting audio transcription into text ...")
        print(text)

    except:
        print("sorry.. run again...")