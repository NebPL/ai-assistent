import lua
import pyttsx3
from datetime import datetime

engine = pyttsx3.init()

#rate = engine.getProperty('rate')      # z. B. 200
#print("Aktuelle Rate:", rate)

callSentence = "hey alexa"

def parseCommand(text):
    if callSentence in text:

        index = text.find(callSentence) 

        if index != -1:
             command = text[index:]  # Alles ab dem Wort inklusive
             execCommand(command)      

def execCommand(command):
    #if comman

    if "uhr" in command:
        engine.setProperty('rate', 175)     
        jetzt = datetime.now()
        uhrzeit = jetzt.strftime("%H:%M")# z. B. 125 = langsamer

        #uhrzeit = jetzt.strftime("%H:%M:%S")# z. B. 125 = langsamer
        engine.say("Es ist: "+uhrzeit)
        engine.runAndWait()

    lua.setCommandVar(command)
    lua.load_lua_files()
    print("Command: " + command)

