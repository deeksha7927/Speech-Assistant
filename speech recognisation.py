import speech_recognition as sr # recognise speech
import playsound # to play an audio file
from gtts import gTTS # google text to speech
import random
from time import ctime # get time details
import webbrowser # open browser
import time
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
        greetings = [f"hey, how can I help you {person_obj.name}", f"hey, what's up? {person_obj.name}", f"I'm listening {person_obj.name}", f"how can I help you? {person_obj.name}", f"hello {person_obj.name}"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        speak(greet)

    # 2: name
    if 'what is your name' in voice_data:
        if person_obj.name:
            speak("my name is Alexis")
        else:
            speak("my name is Alexis. what's your name?")

    if 'my name is' in voice_data:
        person_name = voice_data.split("is")[-1].strip()
        speak(f"okay, i will remember that {person_name}")
        person_obj.setName(person_name) # remember name in person object

    # 3: greeting
    if 'how are you' in voice_data:
        speak(f"I'm very well, thanks for asking {person_obj.name}")

    # 4: time
    if 'what time is it' in voice_data:
        speak(ctime())

    # 5: search google
    if 'search' in voice_data:
        search=record_audio('What do you want to search for?')
        url = 'https://google.com/search?q='+ search
        webbrowser.get().open(url)
        speak('Here is what I found for {search_term} on google'.format(search))

    if 'exit' in voice_data:
        speak("going offline")
        exit()


time.sleep(1)
speak('how can i help you')
while(1):
    voice_data = record_audio() # get the voice input
    respond(voice_data) # respond