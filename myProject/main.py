import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty("voices")
# print(voices[0].id)
engine.setProperty("voices", voices[0].id)
# engine.setProperty("rate", 100)

# will program your SAM to speak something
def say(audio):
    engine.say(audio)
    engine.runAndWait()
#  will make your SAM wish you according to system time
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=5 and hour<12:
        say("Hey, Good Morning")
    elif hour>=12 and hour<16:
        say("Hey, Good Afternoon")
    else:
        say("Hey, Good Evening")

# will allow your SAM to take microphone input from the user and returns a string output
def takeCommand():
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                      
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said :  {query}\n")

    except Exception as e:
        # print(e)
        print("say that again please...")
        return "None"
    return query

def sendEmail(to, content):
    # password = input("Type your password and press enter: ")
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo() # Can be omitted
    server.starttls() # Secure the connection
    server.login("rashmivr14@gmail.com", "keezhillam@123")
    server.sendmail("vrrashmi23@outlook.com", to, content)
    server.close() 

if__init__="__main__"
# say("Hello This is just a test audio")
wishme()
say("I am your personal Voice Assistant Sam. How may I help You?")

while(True):
# if 1:
    query = takeCommand().lower()

    # logic for executing tasks based on query
    if 'wikipedia' in query:
        say("Searching wikipedia...")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences=2)
        say("According to wikipedia")
        print(results)
        say(results)
    
    elif 'open google' in query:
        say("Opening Google")
        webbrowser.open("google.com")
    
    elif 'open youtube' in query:
        say("Opening Youtube. Enjoy!")
        webbrowser.open("youtube.com")
    
    elif 'open instagram' in query:
        say("Opening Instagram")
        webbrowser.open("instagram.com")
    
    elif 'play music' in query:
        musicDir = 'C:\\Users\\vrras\\Music'
        songs = os.listdir(musicDir)
        randomSong =random.choice(songs)
        # print(songs)
        say("Enjoy your playlist")
        os.startfile(f"C:\\Users\\vrras\\Music\\{randomSong}")
        
        # to play first song in the list use below command:
        # print(songs)
        # os.startfile(os.path.join(musicdir, songs[0]))

    elif 'open vs code' in query:
        vscodepath  = "C:\\Users\\vrras\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        say("Opening VS Code")
        os.startfile(vscodepath)
    
    elif 'the time' in query:
        timeNow = datetime.datetime.now().strftime("%H:%M:%S")
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<4:
            say(f"The time is {timeNow} midnight. Its time for you to sleep. Goodnight")
        if hour>=4 and hour<11:
            say(f"The time is {timeNow} in the morning")
        elif hour>=11 and hour<15:
            say(f"The time is {timeNow} in the afternoon")
        elif hour>=15 and hour<20:
            say(f"The time is {timeNow} in the evening")
        elif hour>=15 and hour<24:
            say(f"The time is {timeNow} night")
    
    elif 'email to rashmi' in query:
        try:
            say("What should I say?")
            content = takeCommand()
            to = "vrrashmi23@outlook.com"
            sendEmail(to, content)
            say("email has been sent!")
        except Exception as e:
            print(e)
            say("Sorry Rashmi, I am unable to send this email. Please try again")
    
    elif 'quit' or 'close' in query:
        exit()



