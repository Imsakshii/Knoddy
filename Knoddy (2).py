import pyttsx3 # pip install pyttsx3
import speech_recognition as sr #pip install speechrecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os 

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Knoddy Mam, Please tell me how may I help you")

def takeCommand():
    #It takees microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        #print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == "__main__":
   # speak("Sakshi is a good girl")
   wishMe() # Wish us
   #while True:
   if 1:    
        query = takeCommand().lower()

   # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com") 

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open gfg' in query:
            webbrowser.open("geeksforgeeks.org")

        elif 'play music' in query:
            music_dir = 'D:\\music_dir'
            songs = os.listdir(music_dir) 
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Mam, The time is {strTime})")

        elif 'open code' in query:
            codePath = "C:\\Users\\ahana\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
            os.startfile(codePath)
    
        elif 'open teams' in query:
            TeamsPath = "C:\\Users\\ahana\AppData\\Local\\Microsoft\\Teams\\Update.exe --processStart Teams.exe" 

        elif 'quit' in query or 'bye' in query:
            speak("Quitting Mam, Thanks for your time")