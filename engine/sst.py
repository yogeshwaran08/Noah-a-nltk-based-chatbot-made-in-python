import speech_recognition as sr

def takeCommand(res):
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:

        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:   
        query = r.recognize_google(audio, language ='en-in')
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
     
    res.append(query)