from ast import operator
from calendar import day_abbr, day_name
import time
from urllib import request
import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia 
import webbrowser
import pywhatkit as kit
import smtplib
import sys
import pyjokes
import time
import pyautogui
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtCore import QTimer, QTime, QDate 
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import*
from PyQt5.QtGui import*
from PyQt5.QtWidgets import*
from PyQt5.uic import loadUiType
from jarvisUI import Ui_jarvisUI







engine= pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voices', voices [0].id)

#text to speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()


def wish():
    hour =int(datetime.datetime.now().hour)
    tt = time.strftime("%I:%M %p")
    if hour>=0 and hour<=12:
        speak(f"Good Morning Mr Brighton Chifetete, its {tt}")
    elif hour>=12 and hour<18:
        speak(f"Yo what's up Mr Brighton Chifetete, its {tt}")
    else:
        speak(f"good evening Mr Brighton Chifetete, its {tt}")
    speak("Im jarvis Sir ,  how l can help you today.....")
def sendEmail(to,content):
    server =smtplib.SMTP('smtp.gmail.cim',587)
    server.ehlo()
    server.starttls()
    server.login('your email id','your password')
    server.sendmail('your email id',to ,content)
    server.close()
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcruch&apiKey=094b4e6d2ccd456b8b09ce967d99bbcc'
    main_page = request.get(main_url).json()
    articles = main_page ["articles"]
    head = []
    dat=["first","second","third","fourth","fifth","sixth","seventh","eigth","ninth","tenth"]
    for ar in articles :
        head.append(ar["title"])
    for i in range (len(day_abbr)):
        speak (f"today's {day_name[1]} news is :head[i]")
        
class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
         self.TaskExecution()
   
    def takecommand(self):
        r= sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening......")
            r.pause_threshold=1
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
        try:
            print("Recognizing.......")
            self.query = r.recognize_google(audio, language= 'en-in')
            print(f"user said: {self.query}")
        except Exception as  e:
            #speak("Say that again please...")
            return "none"
        return self.query


    def TaskExecution(self):

        wish()
        #if 1 :
        while True:

            self.query = self.takecommand()
            #logic building for tasks
            if "open notepad" in self.query:
                npath="C:\\WINDOWS\\system32\\notepad.exe"
                os.startfile(npath)

            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam',img)
                    k=cv2.waitKey(500)
                    if k==27:
                        break
                    cap.release()
                    cv2.destroyAllWindows()
            elif "play music" in self.query:
                music_dir ="C:\\Users\\bchifetete\Music\\playlist"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir, song))
            elif "ip address" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"your IP address in{ip}")
            elif "wikipedia" in self.query:
                speak ("searching wikipedia....")
                query = query.replace("wikipedia", "")
                results = wikipedia.summary(self.query , sentences = 2)
                speak("according to wikipedia")
                speak(results)
                print(results)   

            elif  "open command prompt" in self.query:
                os.system("start cmd")
            
            elif"open youtube" in self.query:
                webbrowser.open("www.youtube.com")
            
            elif"open facebook" in self.query:
                webbrowser.open("www.facebook.com")

            elif"open stackoverflow" in self.query:
                webbrowser.open("www.stackoverflow.com")
                
            elif"open google" in self.query:
                speak("Sir , what should l search on google")
                cm = self.takecommand().lower()
                webbrowser.open(f"{cm}")
            elif "send message" in self.query:
                kit.sendwhatmsg("+263787769555" , "this is testing protocol",2,25)

            elif "play song on youtube" in self.query:
                kit.playonyt("south to west")
            elif ("send email ") in self.query:
                try:
                    speak("what should l say?")
                    content = self.takecommand().lower()
                    to = "brightonchifetete@icloud.com"
                    sendEmail(to,content)
                    speak("Email has been send to Brighton")
                except Exception as e:
                    print(e)
                    speak("sorry im unable to send a message to Brighton")
            elif "no thanks" in self.query:
                speak ("thanks for using me sir , have a good day")
                sys.exit()
            elif "sleep" in self.query:
                speak("thanks for using me sir , have a good day")
                sys.exit()

        #to close any application
            elif "close notepad" in self.query:
                speak ("okay sir , closing notepad")
                os.system("taskill /f /im notepad.exe")
        #to set an alarm 
            elif "set alarm" in self.query:
                nn= int(datetime.datetime.now().hour)
                if nn==22:
                    music_dir='E:\\music'
                    songs=os.listdir(music_dir)
                    os.startfile(os.path.join(music_dir, songs[0]))
        #to find a joke
            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)
            elif "shutdown the system" in self.query:
                os.system("shutdown/s /t 5")
            elif "Restart the system " in self.query:
                os.system("shutdown/s /t 5")
            elif "sleep the system" in self.query:
                os.system("rundll32.exe powerprof.dll,SetSuspendState 0,1,0")
            elif 'switch the window' in self.query:
                pyautogui.keydown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            elif "tell me news" in self.query:
                speak("please wait sir , fetching the lates news")
                news()
            elif "do some calculations" in self.query or "can you calculate" in self.query:
                r=sr.Recognizer()
                with sr.Microphone() as source:
                    speak("say what you want to calculate, example : 3 plus ")
                    print("listening.......")
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                my_string=r.recognize_google(audio)
                print(my_string)
                def get_operator_fn(op):
                    return {
                        '+' : operator.add,#plus
                        '-' : operator.sub,#minus
                    }

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_jarvisUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
    def startTask(self):
        self.ui.movie = QtGui.QMovie("C:/Users/administrator/Pictures/iron.gif")
        self.ui.label_3.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
    def showTime(self):
        current_time=QTime.currentTime()
        current_date=QDate.currentDate()
        label_time  = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textEdit.setText(label_date)
        self.ui.textEdit_2.setText(label_time)



app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())









    
               

    #speak("Hello Mr Brighton")

            





















































































































































































































































































































































































































































































































































































































































































































            
         