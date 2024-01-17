import filecmp
import PyPDF2
import fileinput
from httpx import Client
import speech_recognition as sr
import os
import smtplib
import pyttsx3
import sys
import time
import pyautogui
import requests
import tkinter
import json
import pyjokes
import random
import win32
import feedparser
import wolframalpha
import shutil
import ctypes
import wikipedia
import subprocess
import datetime
from selenium import webdriver
from clint.textui import progress
from ecapture import ecapture as ec
from bs4 import BeautifulSoup
import win32com.client as wincl
from urllib.request import urlopen
import webbrowser
import pywhatkit

engine = pyttsx3.init()
engine.runAndWait()
engine.setProperty('rate', 190)

# Set Volume
engine.setProperty('volume', 4.0)

# automated web search code
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    # Enable low security in gmail
    server.login('labpractical121@gmail.com', 'qwqprathameshqwq')
    server.sendmail('labpractical121@gmail.com', to, content)
    server.close()

def greet():
    # Greets the user according to the tim
    speak("system is live, how are you doing sir.")

try:
    print("checking requirements.")
    # check the mic availability and proceed
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("microphone is ready")
except:
    print("i won't be able to take commands sir if your microphone is not connected. Please connect a microphone and try again :)")
    speak("i won't be able to take commands sir if your microphone is not connected. Please connect a microphone and try again.")
    quit()

def open_cmd():
    os.system('start cmd')

def playmusic():
    speak("provide me with the song name please")
    query = takeCommand()
    pywhatkit.playonyt(query)

def takeCommand():
    # start listening the command from the user
    with sr.Microphone() as source:
        print("Please wait.. ")
        print("listening....")
        r.energy_threshold = 4000
        r.dynamic_energy_threshold = True
        audio = r.listen(source)

    try:
        print("recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"you said: {query}\n")
    except Exception as e:
        print("Say that again ,please")
        speak("say that again please")
        return "None"
    return query

if __name__ == "__main__":
    greet()
    while True:
        query = takeCommand().lower()
        
        # GREETING QUERY
        if 'hello ' in query:
            speak("hello sir how are you doing these days")
            query = takeCommand()
            
        if 'good' in query:
            speak("i am glad to hear that sir.")
            speak("how would you like to spend time sir. wanna hear some music, wanna get knowledge about something"
            + "ask me anything sir ")
            query = takeCommand()

        elif 'music' in query:
            playmusic()

        # JARVIS ORTHODOX QUIT QUERY
        elif 'quit' in query:
            speak("thanks for having me ")
            quit()

        elif 'fuck off' in query:
            speak("thanks for having me ")
            quit()

        elif 'get lost' in query:
            speak("thanks for having me ")
            quit()

        elif 'you can go' in query:
            speak("thanks for having me ")
            quit()

        # JARVIS QUIT FUNCTION
        if 'jarvis quit' in query:
            speak("thanks for having me ")
            quit()

        elif 'jarvis tweet' in query:
            speak("if you say so. just call me if you need me")

        # CLEARING DATA FROM FILES CODE
        elif 'clear data from file' in query:
            file = open('said.txt', 'r')
            file.write("data is cleared :)")

        # WIKIPEDIA CODE
        elif 'wikipedia' in query:
            try:
                query = query.replace("wikipedia", "")
                result = wikipedia.summary(query, sentences=2)
                print("according to wikipedia")
                print(result)
                speak("according to wikipedia.")
                speak(result)
            except:
                speak("no such thing found on wikipedia. sorry")

        # DESTRY DATA QUERY
        elif 'destroy' in query:
            speak("data destruction  initializing....")
            speak(" destroying data from text file..")
            file = open('said.txt', '')
            file.write("data cleared ")
            speak("task completed")
            file.close()

        # THANKS QUERY CODE
        elif 'thanks' in query:
            speak("any time sir")
            quit()

        elif 'open command prompt' in query:
            speak("on it sir.")
            open_cmd()

        # DATA ENCRYTING CODE
        elif 'encrypt' in query:
            speak("select the file from above mentioned files")
            tupls = ("file1.txt", "file2.txt", "file3.txt")
            print(tupls)

        # SEARCH AUTOMATION USING SELENIUM
        elif 'search' in query or 'open google' in query:
            speak("what do you want me to search sir.")
            query = takeCommand()
            try:
                webbrowser.open("https://www.google.com/search?q="+query)
            except:
                speak("couldn't open browser.")

        elif 'open google' in query:
            try:
                webbrowser.open("https://www.google.com/search?q=")
            except:
                speak("something went wrong check the code.")

        elif 'youtube' in query:
            speak("what do you want me to play on youtube sir")
            query = takeCommand()
            try:
                pywhatkit.playonyt(query)
            except:
                speak("couldn't open the youtube")

        elif 'play some songs' in query or 'play songs' in query or 'music' in query:
            pywhatkit.playonyt("The Weeknd")

        elif 'play some stand up' in query:
            speak("which video you wanna laugh on sir")
            query = takeCommand()
            pywhatkit.playonyt(query)

        elif 'play this song' in query:
            playmusic()

        elif 'tell me about' in query:
            takeCommand()
            try:
                pywhatkit.info(query, lines=4)
                speak()
                print("\nSuccessfully Searched")
            except:
                print("An Unknown Error Occurred")

        elif 'take screen shot' in query or 'take screenshot' in query or 'snap' in query:
            myScreenshot = pyautogui.screenshot()
            myScreenshot.save(r'C:\Users\Public\Desktop\python projects\screenshot.png')

        elif 'open stackoverflow' in query or 'open stack overflow' in query:
            speak("Here you go to Stack Over flow.Happy coding")
            webbrowser.open("stackoverflow.com")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("% H:% M:% S")
            speak(f"Sir, the time is {strTime}")
        elif 'open opera' in query:
                codePath ="link"
                os.startfile(codePath)
        elif 'email to Naveen' in query:
             try:
                 speak("What should I say?")
                 content = takeCommand()
                 to = "navingarje5@gmail.com"
                 sendEmail(to, content)
                 speak("Email has been sent !")
             except Exception as e:
                 print(e)
                 speak("I am not able to send this email")
        elif 'send a mail' in query:
             try:
                 speak("What should I say?")
                 content = takeCommand()
                 speak("whome should i send")
                 to = input()
                 sendEmail(to, content)
                 speak("Email has been sent !")
             except Exception as e:
                 
                 print(e)
                 speak("I am not able to send this email")
        elif 'how are you' in query:
             
             speak("I am fine, Thank you")
             speak("How are you, Sir")
        elif 'fine' in query or "good" in query:
             speak("It's good to know that your fine")
        elif "change my name to" in query:
             query = query.replace("change my name to", "")
             assname = query
        elif "change name" in query:
             speak("What would you like to call me, Sir ")
             assname = takeCommand()
             speak("Thanks for naming me")
        elif "what's your name" in query or "What is your name" in query:
             speak("My friends call me")
             speak(assname)
             print("My friends call me", assname)
        elif 'exit' in query:
             speak("Thanks for giving me your time")
             exit()
        elif 'joke' in query:
             speak(pyjokes.get_joke())
        elif "calculate" in query:
             app_id = "Wolframalpha api id"
             client = wolframalpha.Client(app_id)
             indx = query.lower().split().index('calculate')
             query = query.split()[indx + 1:]
             res = client.query(' '.join(query))
             answer = next(res.results).text
             print("The answer is " + answer)
             speak("The answer is " + answer)
        elif 'search' in query or 'play' in query:
             query = query.replace("search", "")
             query = query.replace("play", "")
             webbrowser.open(query)
        elif "who i am" in query:
             speak("i am one of the many prototypes you have designed sir, you are supreme lord who designed me and developed me with time.")
        elif "why you came to world" in query:
             speak("i am a part of a project currently developed by mr.cipherNomad. thats all i know")
        elif 'power point presentation' in query or 'powerpoint presentation' in query:
             try:
                speak("opening Power Point presentation")
                power = r"C:\ProgramData\Microsoft\Windows\StartMenu\Programs\PowerPoint.lnk"
                os.startfile(power)
             except:
                 speak("oops! encountered an error mind fixing it sir, bacause i can't")
                 print("oops! encountered an error mind fixing it sir, bacause i can't")

        elif 'change background' in query:
             ctypes.windll.user32.SystemParametersInfoW(20,0,"Location of wallpaper",0)
             speak("Background changed successfully")
        elif 'open bluestack' in query:
             appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
             os.startfile(appli)
        elif 'news' in query:
            try:
                jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy =top&apiKey =\\times of India Api key\\''')
                data = json.load(jsonObj)
                i = 1
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============''' + '\n')
                for item in data['articles']:
                    
                    (str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                print(str(e))
        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()
        elif 'shutdown system' in query:
            speak("Hold On a Sec ! Your system is on its way to shut down")
            subprocess.call('shutdown / p /f')

        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop jarvis from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
        elif "where is" in query or 'locate' in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.com/maps/place/" + location)
        elif "camera" in query or "take a photo" in query:
            ec.capture(0, "Jarvis Camera ", "img.jpg")
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            speak("now shutting down the sub processes in the system.")
            subprocess.call("shutdown / h")
        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
        elif "show note" in query:
                speak("Showing Notes")
                file = open("jarvis.txt", "r")
                print(file.read())
                speak(file.read(6))
        elif "update assistant" in query:
                speak("After downloading file please replace this file with the downloaded one")
                url = '# url after uploading file'
                r = requests.get(url, stream=True)
                with open("Voice.py", "wb") as Pypdf:
                    total_length = int(r.headers.get('content-length'))
                    for ch in progress.bar(r.iter_content(chunk_size=2391975),expected_size=(total_length / 1024) + 1):
                        if ch:
                            Pypdf.write(ch)
        elif "weather" in query:
 # Google Open weather website
 # to get API of Open weather
                try:
                    api_key = "073f1e2264d42a1b5d93a4d9347631f8"
                    base_url = "http://api.openweathermap.org/data/2.5/weather?"
                    speak(" City name ")
                    print("City name : ")
                    city_name = input()
                    complete_url = base_url + "appid =" + api_key + "&q =" + city_name
                    response = requests.get(complete_url)
                    x = response.json()
                    if x["code"] != "404":
                        y = x["main"]
                        current_temperature = y["temp"]
                        current_pressure = y["pressure"]
                        current_humidiy = y["humidity"]
                        z = x["weather"]
                        weather_description = z[0]["description"]
                        print(" Temperature (in kelvin unit) = " + str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) + "\n humidity (in percentage) = " + str(current_humidiy) + "\ndescription = " + str(weather_description))
                    else:
                        speak(" City Not Found ")
                except:
                    print("failed to find the weather.")
                    speak("failed to find the weather details.")

         
        elif 'send text message' in query:
                    try:
                        speak("What do you want me to say?")
                        body_msg = takeCommand()
    
    # Assume you want to get the receiver's number from the user's voice input
                        speak("Who is the receiver? Please provide the number.")
                        receiver = input()
                
                # Your Twilio account SID and auth token
                        account_sid = 'AC1b16ea2d04ae918b9d99f4c645452fb1'
                        auth_token = '[AuthToken]'
                
                # Twilio phone number
                        twilio_number = '+19283796099'
                
                # TwiML Messaging API endpoint
                        endpoint = f'https://api.twilio.com/2010-04-01/Accounts/{account_sid}/Messages.json'
                
                # Parameters for sending the message
                        data = {
                            'To': receiver,
                            'From': twilio_number,
                            'Body': body_msg,
                        }
                
                # Perform the API request
                        response = requests.post(endpoint, auth=(account_sid, auth_token), data=data)
                    except:
                        speak("couldn't send message")
            
        elif "wikipedia" in query:
            webbrowser.open("wikipedia.com")
        elif "Good Morning" in query:
            speak("A warm" + query)
            speak("How are you sir")
            speak(assname)
# most asked question from google Assistant
        elif "will you be my gf" in query or "will you be my bf" in query:
            speak("I'm not sure about, may be you should give me some time")
        elif "how are you" in query:
            speak("I'm fine, glad you asked")
        elif "i love you" in query:
            speak("It's hard to understand")
        elif 'what is temperature' in query:
            speak("which city's temperature do you want to know.")
            city = takeCommand()
            print(city)
            speak("user asked for {city}")
def get_temperature(city):
    api_key = 'a9b639d53ead803eeaee28694b16e5e2'
    url =f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    data = response.json()
    temperature = data['main']['temp']
    return temperature
    temperature = get_temperature(city)
    print(f'The temperature in {city} is {temperature}°C.')
