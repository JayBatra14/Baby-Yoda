import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random
import subprocess
from twilio.rest import Client 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("I am Baby Yoda. Please tell me Sir how may I help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception:
        print("Say that again please...")
        return "None"
    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.ehlo()
    server.starttls()
    server.login('yourid','password')
    server.sendmail('yourid',to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    contacts={"self":"your_phone_number"}
    while(1):
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query=query.replace("wikipedia","") 
            results=wikipedia.summary(query,sentences=2)
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            speak("opening youtube")
            webbrowser.open_new_tab('https://www.youtube.com')
            #webbrowser.open("youtube.com")

        elif 'open google' in query:   
            speak("opening google")
            webbrowser.open_new_tab('https://www.google.com')
            #webbrowser.open("google.com")

        elif 'open stack overflow' in query:
            speak("opening stack overflow")
            webbrowser.open_new_tab('https://www.stackoverflow.com')
            #webbrowser.open("stackoverflow.com")
           

        elif 'search' in query or 'सर्च' in query:
            speak("tell me what you want to search")
            google=takeCommand()
            webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % google)

        #elif 'सर्च' in query:
            #speak("tell me what you want to search")
            #google=takeCommand()
            #webbrowser.open_new_tab('http://www.google.com/search?btnG=1&q=%s' % google)

        elif 'play music' in query:
            music_dir='D:\\music' 
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))
        
        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codepath="Code.exe"
            os.startfile(codepath)
        
        elif 'whatsapp' in query:
            speak('to whom you want to send the msg')
            name=takeCommand()
            if name in contacts:
                speak('What should I say')
                content=takeCommand()
                account_sid = 'your_sid' 
                auth_token = 'your_token' 
                client = Client(account_sid, auth_token) 
 
                client.messages.create( 
                              body=content, 
                              from_='whatsapp:your_twilio_number',      
                              to='whatsapp:' +contacts[name] 
                          ) 
            else:
                speak("Invalid name")

        elif 'toss' in query:
            result=random.choice(('head','tail'))
            speak(result)
            print(result)

        elif 'dice' in query:
            result=random.choice((1,2,3,4,5,6))
            speak(result)
            print(result)

        elif 'play' in query:
            speak("ready")
            for i in range(3):
                speak("stone paper scissor")
                engine.runAndWait() 
                result=random.choice(('stone','paper','scissor'))
                speak(result)
                print(result)

        elif 'email to jatin' in query:
            try:
                speak('What should I say')
                content=takeCommand()
                to="youremail@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")
            except Exception as e:
                print(e)
                speak("Sorry I am not able to send this email")

        elif 'camera' in query:
            cmd="start microsoft.windows.camera:"
            subprocess.call(cmd, shell=True)

        elif 'off' in query:
            speak("Ok have a nice day Sir")
            os._exit(0)
        

    
