***This program was developed and written by Zebulon C Ute 
This was an example tutorial for YouTube
http://github.com/Graemelaurie84/JarvisCode***

***Notes***

#Libraries-------------------------------------------------------------------
import pyttsx3
import speech_recognition as sr
import time
from openpyxl import
import random


***varlables**
r = sr.Recognizer()
keywords = [("jsrvis", 1). ("hey jarvis", 1). ]
source = sr.Microphone()


#Functions-------------------------------------------------------------------
def Speak(text):
    rate = 100
    engine = pyttsx3.init()
    voiice = engine.getProperty("voice")
    engine.setProperty("voice" , voices[0].id)
    engine.setProperty("rate" , rate=50)
    engine.say(text)
    engine.runAndWait()
def callback(recognizer, audio):
    try:
       speach_as_text = recognizer.recognize_sphinx(audio, keywords_entries-keywords)
       print(speach_as_text)
    if "jarvis" in_speach_as_text or "hey jarvis":
        Speak("Yes sir?")
        recognize_main()
    except sr.UnknownValueError:
    print("Oops! Didn't catch that")
def start_recognizer():
    print("waiting for a keyword...Jarvis or Hey Jarvis")
    r.listen_in_background(source, callback)
    time.sleep(1000000)
def recognize_main():
    r = sr.recogizer()
    with sr_Microphone() as source:
    print("Say something!")
    audio = r_listen(source)
    data = ""
    try:
       data = r.recognize_google(audio)
       data.lower()
       print("You said: " + data)
#Greetings------------------------------------------------------------------
    if "how are you" in data:
        Speak("I am Fine")
    elif "hello" in data:
        Speak ("Hi there")
    else:
        Speak("I'm sorry sir, I did not understand your request")
    except sr.UnknownValueError:
    print("Jarvis did not understand your request")
    except sr.RequestError as e:
    print("Could not request results from Google Speach Recogniyionservice; {0}".format(e))
def excel():
    wb = load_workbook("imput.xlsx")
    wu = wb.get_sheet_by_name("User")
    wr = wb.get_sheet_by_name("Replies")


    global hello_list
    global how_are_you
    urow1 = wu["1"]
    urow2 = wu["2"]
    hello_list = [urow1[x].value for x in range(len(urow1))]
    how_are_you = [urow2[x].value for x in range(len(urow2))]


    global reply_hello_list
    global reply_how_are_you
    rrow1 = wr["1"]
    rrow2 = wr["2"]
    reply_hello_list = [rrow1[x].value for x in range(len(urow1))]
    reply_how_are_you = [rrow2[x].value for x in range(len(urow2))]



#Main program----------------------------------------------------------------
while 1:
    start_recognizer()
#Notes-----------------------------------------------------------------------