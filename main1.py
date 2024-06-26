import speech_recognition as sr
import webbrowser
import pyttsx3 
import musiclibrary
import requests


recognizer=sr.Recognizer()
engine = pyttsx3.init()
newsapi="********************"

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musiclibrary.music[song]
        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            # Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles', [])
            
            # Print the headlines
            for article in articles:
                speak(article['title'])
    
if __name__ == "__main__": 
    speak("Initializing Mini Alexa....")
    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()
        print("recognizing...")
        # recognize speech using google
        try:
           with sr.Microphone() as source:
              print("Listening...")
              audio = r.listen(source,timeout=2,phrase_time_limit=1)
           word=r.recognize_google(audio)
           if (word.lower()=="Alexa"):
               speak("Hi I am Mini Alexa How may I help you")
               with sr.Microphone() as source:
                   print("Mini Alexa Active...")
                   audio = r.listen(source)
                   command=r.recognize_google(audio)
                   processCommand(command)
        except Exception as e:
           print("Error; {0}".format(e))
