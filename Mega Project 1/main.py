import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests

recognizer = sr.Recognizer()        # Make a Recognizer 
engine = pyttsx3.init()             # Initialize the pyttsx
newsapi = "bc55b5edd5124354a5f720cd5937b4df"


def speak(text):                    # Function so that he can speak to user 
    engine.say(text)
    engine.runAndWait()             # By this we can run and wait the speak

def processCommand(c):
    if "open google" in c.lower() :
        webbrowser.open("https://google.com")

    elif "open facebook" in c.lower() :
        webbrowser.open("https://facebook.com")
    
    elif "open linkedin" in c.lower() :
        webbrowser.open("https://linkedin.com")

    elif "open youtube" in c.lower() :
        webbrowser.open("https://youtube.com")

    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get("https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")

        if r.status_code == 200:
            #   Prase the JSON response
            data = r.json()

            # Extract the article
            articles = data.get('article',[])

            # Print the headlines
            for article in articles :
                speak(article['title'])

    else:
        # Let open AI Handle the request
        pass

if __name__ == "__main__" :
    speak("Initializing Jarvis....")

    while True:

        # Listen for the wake word Jarvis
    
        # obtain audio from the microphone
        r = sr.Recognizer()
        

        print("recognizing.....")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source, timeout= 2 , phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower()== "jarvis"):
                speak("Ya please tell")

                #Listen for command 
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand()


        except Exception as e:
         print("Error; {0}".format(e))
    
