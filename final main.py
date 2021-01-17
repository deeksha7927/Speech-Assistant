import speech_recognition as sr # recognise speech
import playsound # to play an audio file
from gtts import gTTS # google text to speech
import random
from time import ctime # get time details
import webbrowser # open browser
import time
import pywhatkit
import wikipedia
import pyjokes
import os # to remove created audio files

r = sr.Recognizer() # initialise a recogniser
# listen for audio and convert it to text:
def record_audio(ask=False):
    with sr.Microphone() as source: # microphone as source
        if ask:
            speak(ask)
        audio = r.listen(source)  # listen for the audio via source
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)  # convert audio to text
        except sr.UnknownValueError: # error: recognizer does not understand
            speak('I did not get that')
        except sr.RequestError:
            speak('Sorry, the service is down') # error: recognizer is not connected
        return voice_data

# get string and make a audio file to be played
def speak(audio_string):
    tts = gTTS(text=audio_string, lang='en') # text to speech(voice)
    r = random.randint(1,20000000)
    audio_file = 'audio' + str(r) + '.mp3'#creating audio file
    tts.save(audio_file) # save as mp3
    playsound.playsound(audio_file) # play the audio file
    print(audio_string) # print what app said
    os.remove(audio_file) # remove audio file

def respond(voice_data):
    if 'hi' in voice_data:
        speak('hello')

    # 2: name
    if 'what is your name' in voice_data:
            speak('my name is Alexis.')

    # 2: greeting
    if 'how are you' in voice_data:
        speak('I am very well, thanks for asking')

    # 3: time
    if 'time' in voice_data:
        speak(ctime())

    # 4: search google
    if 'search' in voice_data:
        speak('What do you want to search for?')
        search=record_audio()
        url = 'https://google.com/search?q='+ search
        webbrowser.get().open(url)
        speak('here is what i found for' + search)
    # 5: play music
    if 'play' in voice_data:
        speak('which song do you want to play')
        song=record_audio()
        pywhatkit.playonyt(song)
    # 6: search wikipedia
    if 'wikipedia' in voice_data:
        speak('what do you want to search in wikipedia')
        person=record_audio()
        info=wikipedia.summary(person,1)
        print(info)
    # 7: jokes
    if 'jokes' in voice_data:
        speak(pyjokes.get_joke())
    # 8: search location
    if 'location' in voice_data:
        speak('what is the location')
        location=record_audio()
        url='https://google.nl/maps/place/'+location
        webbrowser.get().open(url)
        speak('here is what i found for'+location)
    # 9: exit
    if 'exit' in voice_data:
            speak("going offline")
            exit()

time.sleep(1)
speak('how can i help you')
while(1):
    voice_data = record_audio() # get the voice input
    respond(voice_data) # respond