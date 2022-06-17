import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia


engine =pyttsx3.init('sapi5')
voices =engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[0].id)



def speak(audio):
   engine.say(audio)
   engine.runAndWait()


def wishMe():
    hour =int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good moring")
    elif hour>=12 and hour<18:
        speak("good afternoon")

    else:
        speak("Good evening")

    speak("I am jarvis sir please tell me how may i help you")


def takecommand():
    #it take microphone input from the user#
   
   
    r=sr.Recognizer
    with sr.Microphone() as source:
        print("Listening........")
        r.pause_threshold=1
        audio=r.listen(source)

    

    try:
        print("Recognizing....")
        query=r.recognize_google(audio, Language='en-in')
        print(f"user said:{query}\n")

    except Exception as E:
        #print(e)
        print("SAY THAT AGAIN PLEASE....")
        return "None"
    return query   


if __name__=="__main__":
    wishMe()
    while True:
        query=takecommand().lower()

        if 'wikipedia' in query:
            speak('searching wikipedia....')
            query = query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("according tp wikipedia")
            speak(results)


