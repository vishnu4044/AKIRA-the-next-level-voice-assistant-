import speech_recognition as sr  # importing speech recognition package from google api
import datetime # date time
import playsound    # to play saved mp3 file
from gtts import gTTS   # google text to speech
import os   # to save/open files
import wolframalpha # to calculate strings into formula, its a website which provides api, 100 times per day
import webbrowser#browser
import wikipedia#wikipedia
import tkinter as tk
from tkinter import *

window =Tk()
num = 1

text =StringVar()

def assistant_speaks(output):
    global num
    num +=1
    print("PerSon : ", output)
    toSpeak = gTTS(text=output, lang='en-US', slow=False)
    file = str(num)+".mp3"
    toSpeak.save(file)
    playsound.playsound(file, True)
    os.remove(file)
def speechaudi()-> object:

    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak1...")
        audio = r.listen(source)
    if audio =="Akira stop":
        print("Stop.")
    try:
        text = r.recognize_google(audio, language='en-US')
        print("You : ", text)
        return text
    except:
        return cmd()
def speechtxt(input):
    assistant_speaks("name of your file")
    filename=get_audio()
    red = filename
    blue='.word'
    fob=open('C:/Users/Public/'+red+blue,'w')
    assistant_speaks("start content")
    hnh=speechaudi()
    stopwords = ['Akira', 'stop', 'akira', '', '']
    querywords = hnh.split()

    resultwords = [word for word in querywords if word.lower() not in stopwords]
    result = ' '.join(resultwords)
    fob.write(result)
    fob.close()
    assistant_speaks("your  word file is saved in c drive user  public")
    os.startfile('C:/Users/Public/' + red + blue)
    return online()

def get_audio() -> object:
    r = sr.Recognizer()
    audio = ''
    with sr.Microphone() as source:
        print("Speak...")
        audio = r.listen(source, phrase_time_limit=5)
    print("Stop.")
    try:
        text = r.recognize_google(audio,language='en-US')
        print("You : ", text)
        return text
    except:
           return cmd()

def swio(input):
    assistant_speaks("Opening in swiggy")
    assistant_speaks("what kind of will you take")
    result = get_audio()
    if result:
        domain = result
        url = 'https://www.swiggy.co.in/search?q=' + domain
        webbrowser.open(url)
        return

def zito(input):
    assistant_speaks("Opening in zomato")
    assistant_speaks("what kind of food will you take")
    query = get_audio()
    result = query
    if result:
        domain = result
        url = 'https://www.zomato.co.in/search?q=' + domain
        webbrowser.open(url)
        return

def exist(input):
    if os.path.exists("C:/Users/Public/clean.bat"):
        os.startfile("C:/Users/Public/clean.bat")
        os.startfile("C:/Users/Public/clean2.bat")
    else:
        return clean(input.lower())
def florder(input):
    assistant_speaks("creating a folder in system")
    assistant_speaks("give me a name to folder in system")
    vng ="C:/Users/Public/"
    ans = get_audio()
    os.mkdir(vng+ans)
    assistant_speaks("created a folder in system")
    return
def clean(input):
 fob = open('C:/Users/Public/clean.txt', 'w')
 fob.write("@echo off \n"
              " color a \n"
              "echo WELCOME TO GmatriX\n"
             "c:\n"
              "a:\n"
              "attrib -h -r -s -a /s /d a:\*.*\n"
              "del *.lnk\n"
              "del *.vbs\n"
              "del *.inf\n"

              "c:\n"
              "b:\n"
              "attrib -h -r -s -a /s /d b:\*.*\n"
              "del *.lnk\n"
              "del *.vbs\n"
              "del *.inf\n"

              "c:\n"
              "e:\n"
              "attrib -h -r -s -a /s /d e:\*.*\n"
              "del *.lnk\n"
              "del *.vbs\n"
              "del *.inf\n"

              "c:\n"
              "f:\n"
              "attrib -h -r -s -a /s /d f:\*.*\n"
              "del *.lnk\n"
              "del *.vbs\n"
              "del *.inf\n"

              "c:\n"
              "g:\n"
              "attrib -h -r -s -a /s /d g:\*.*\n"
              "del *.lnk\n"
              "del *.vbs\n"
              "del *.inf\n"

              "c:\n"
              "h:\n"
              "attrib -h -r -s -a /s /d h:\*.*\n"
              "del *.lnk\n"
              "del *.vbs\n"
              "del *.inf\n"

              "c:\n"
              "i:\n"
              "attrib -h -r -s -a /s /d i:\*.*\n"
              "del *.lnk\n"
              "del *.vbs\n"
              "del *.inf\n"

              "c:\n"
              "j:\n"
              "attrib -h -r -s -a /s /d j:\*.*\n"
              "del *.lnk\n"
              "del *.vbs\n"
              "del *.inf\n"

              "c:\n"
              "k:\n"
              "attrib -h -r -s -a /s /d k:\*.*\n"
              "del *.lnk\n"
              "del *.vbs\n"
              "del *.inf\n"

              "c:\n"
              "l:\n"
              "attrib -h -r -s -a /s /d m:\*.*\n"
              "del *.lnk\n"
              "del *.vbs\n"
              "del *.inf\n"

              "c:\n"
              "n:\n"
              "attrib -h -r -s -a /s /d n:\*.*\n"
              "del *.lnk\n"
              "del *.vbs\n"
              "del *.inf\n"

              "c:\n"
              "o:\n"
              "attrib -h -r -s -a /s /d o:\*.*\n"
              "del *.lnk\n"
              "del *.vbs\n"
              "del *.inf\n"

              "c:\n"
              "p:\n"
              "attrib -h -r -s -a /s /d p:\*.*\n"
              "del *.lnk\n"
              "del *.vbs\n"
              "del *.inf\n"

              "c:\n"
              "q:\n"
              "attrib -h -r -s -a /s /d q:\*.*\n"
              "del *.lnk\n"
              "del *.vbs\n"
              "del *.inf\n"

              "c:\n"
              "r:\n"
              "attrib -h -r -s -a /s /d r:\*.*\n"
              "del *.lnk\n"
              "del *.vbs\n"
              "del *.inf\n"

              "c:\n"
              "s:\n"
              "attrib -h -r -s -a /s /d s:\*.*\n"
              "del *.lnk\n"
              "del *.vbs\n"
              "del *.inf\n"

              "c:\n"
              "t:\n"
              "attrib -h -r -s -a /s /d t:\*.*\n"
              "del *.vbs\n"
              "del *.inf\n"

              "del *.lnk\n"
              "del *.vbs\n"
              "del *.inf\n"

              "c:\n"
              "u:\n"
              "attrib -h -r -s -a /s /d u:\*.*\n"
              "del *.lnk\n"
              "del *.vbs\n"
              "del *.inf\n"

              "c:\n"
              "v:\n"
              "attrib -h -r -s -a /s /d v:\*.*\n"
              "del *.lnk\n"
              "del *.vbs\n"
              "del *.inf\n"

              "c:\n"
              "w:\n"
              "attrib -h -r -s -a /s /d w:\*.*\n"
              "del *.lnk\n"
              "del *.vbs\n"
              "del *.inf\n"

              "c:\n"
              "x:\n"
              "attrib -h -r -s -a /s /d x:\*.*\n"
              "del *.lnk\n"
              "del *.vbs\n"
              "del *.inf\n"

              "c:\n"
              "y:\n"
              "attrib -h -r -s -a /s /d y:\*.*\n"
              "del *.lnk\n"
              "del *.vbs\n"
              "del *.inf\n"

              "c:\n"
              "attrib -h -r -s -a /s /d w:\*.*\n"
              "del *.lnk\n"
              "del *.vbs\n"
              "del *.inf\n"

              "c:\n"
              "x:\n"
              "attrib -h -r -s -a /s /d x:\*.*\n"
              "del *.lnk\n"
              "del *.vbs\n"
              "del *.inf\n"

              "c:\n"
              "y:\n"
              "attrib -h -r -s -a /s /d y:\*.*\n"
              "del *.lnk\n"
              "del *.vbs\n"
              "del *.inf\n"

              "c:\n"
              "z:\n"
              "attrib -h -r -s -a /s /d z:\*.*\n"
              "del *.lnk\n"
              "del *.vbs\n"
              "del *.inf\n"
              "echo VIRUS IS REMOVED\n")
 fob.close()
 clean2(input.lower())

def clean2(input):
  fob = open('C:/Users/Public/clean2.txt', 'w')
  fob.write("@echo off\n"
              "title Antivirus By Akira\n"
               "echo Antivirus\n"
              "echo Created By TheTechTrax\n"
              "echo scanning....\n"
              "echo scanning....\n"
              ":start\n"
             "IF EXIST virus.bat goto infected\n"
             "IF NOT EXIST virus.bat goto clean\n"
             "cd C:\Windows\system32\n"
              ":infected\n"
            "echo WARNING VIRUS DETECTED!\n"
             "del virus.bat"
              "pause\n"
              "goto start\n"
               ":clean\n"
          "echo System Protected!\n"
           "echo CREDITS: TheTechTrax By Akria\n"
             "exit")
  fob.close()
  os.rename("C:/Users/Public/clean.txt", "C:/Users/Public/clean.bat")
  os.rename("C:/Users/Public/clean2.txt", "C:/Users/Public/clean2.bat")
  assistant_speaks("cleaning started")
  return



def open_application(input):
    if "chrome" in input:
        assistant_speaks("Google Chrome")
        os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
        return
    elif "firefox" in input or "mozilla" in input:
        assistant_speaks("Opening Mozilla Firefox")
        os.startfile('C:\Program Files\Mozilla Firefox\\firefox.exe')
        return
    elif "word" in input:
        assistant_speaks("Opening Microsoft Word")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Word 2013.lnk')
        return
    elif "excel" in input:
        assistant_speaks("Opening Microsoft Excel")
        os.startfile('C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Microsoft Office 2013\\Excel 2013.lnk')
        return
    elif "netflix" in input:
        assistant_speaks("Opening netflix")
        url = 'http://www.netflix.com/Search?v1=Jaws'
        webbrowser.open(url)
        return
    elif "hotstar" in input:
        assistant_speaks("Opening netflix")
        url = 'https://www.hotstar.com'
        webbrowser.open(url)
        return
    elif "prime" in input:
        assistant_speaks("Opening netflix")
        url = 'https://www.primevideo.com'
        webbrowser.open(url)
        return
    else:
        assistant_speaks("Application not available")
        return
def youtube(input):
        assistant_speaks("Opening in youtube")
        query = input.lower()
        stopwords = ['play', 'youtube', 'in', 'on', 'at']
        querywords = query.split()

        resultwords = [word for word in querywords if word.lower() not in stopwords]
        result = ' '.join(resultwords)

        if result:
            domain = result
            url = 'https://www.youtube.com/results?search_query=' + domain
            webbrowser.open(url)
            return

def weather(input):
    assistant_speaks("which city weather do you want to know")
    pop = get_audio()
    if pop:
        domain = pop
        url = 'http://api.openweathermap.org/data/2.5/weather?appid=0c42f7f6b53b244c78a418f4f181282a&q=' + domain
        webbrowser.open(url)
        return

def swiggy (input):
    assistant_speaks("Opening in amazon")
    query = input.lower()
    stopwords = ['place', 'in', 'swiggy', 'order', 'a']
    querywords = query.split()

    resultwords = [word for word in querywords if word.lower() not in stopwords]
    result = ' '.join(resultwords)
    if result:
        domain = result
        url = 'https://www.swiggy.com/search?q=' + domain
        webbrowser.open(url)
        return


def search(input):

            assistant_speaks("Opening in chrome")
            query = input.lower()
            stopwords = ['search', 'about', '', '', '']
            querywords = query.split()

            resultwords = [word for word in querywords if word.lower() not in stopwords]
            result = ' '.join(resultwords)
            if result:
                domain = result
                url = 'https://www.google.co.in/search?q='+domain
                webbrowser.open(url)
                return

def close(input):
    query = input.lower()
    stopwords = ['close', 'Application', '', '', '']
    querywords = query.split()

    resultwords = [word for word in querywords if word.lower() not in stopwords]
    result = ' '.join(resultwords)
    if result:
        domain = result
        assistant_speaks("closeing"+domain)
        os.system("TASKKILL /F /IM " +domain +".exe")
        return

def zomato(input):
    assistant_speaks("Opening in amazon")
    query = input.lower()
    stopwords = ['place', 'in', 'swiggy', 'order', 'a']
    querywords = query.split()

    resultwords = [word for word in querywords if word.lower() not in stopwords]
    result = ' '.join(resultwords)
    if result:
        domain = result
        url = 'https://www.zomato.com/search?q=' + domain
        webbrowser.open(url)
        return


def flipkart(input):
    assistant_speaks("Opening in flipkart")
    query = input.lower()
    stopwords = ['shop', 'in', 'flipkart', '', '']
    querywords = query.split()

    resultwords = [word for word in querywords if word.lower() not in stopwords]
    result = ' '.join(resultwords)
    if result:
        domain = result
        url = 'https://www.flipkart.com/search?q=' + domain
        webbrowser.open(url)
        return

def amazon (input):
    assistant_speaks("Opening in amazon")
    query = input.lower()
    stopwords = ['shop', 'in', 'amazon', '', '']
    querywords = query.split()

    resultwords = [word for word in querywords if word.lower() not in stopwords]
    result = ' '.join(resultwords)
    if result:
        domain = result
        url = 'https://www.amazon.in/s?k=' + domain
        webbrowser.open(url)
        return



def wiki(input):
    query = input.lower()
    stopwords = ['what', 'about', 'mean', '', '']
    querywords = query.split()

    resultwords = [word for word in querywords if word.lower() not in stopwords]
    result = ' '.join(resultwords)
    if result:
        domain="ufufuugu"
        domain = result
        assistant_speaks(wikipedia.summary(domain, sentences=1))
        return

def cmd():
    cmdi = get_audio()
    if cmdi == "Akira":
        assistant_speaks("what can i do for you")
        tata()
    else:
         online()
    return

def online():

    voice = get_audio()
    if voice == "Akira":
        assistant_speaks("what can i do for you")
        text = get_audio().lower()
        if text == 0:
            assistant_speaks(text)

        if "exit" in str(text) or "bye" in str(text) or "go " in str(text) or "sleep" in str(text):
            assistant_speaks("Ok bye, "'.')
            quit()
        process_text(text)
        while (1):
            tata()

    else:
        get_audio()
    return
def tata():
    while (1):
        text = get_audio().lower()
        if text == 0:
            continue
        assistant_speaks(text)
        if "exit" in str(text) or "bye" in str(text) or "go " in str(text) or "sleep" in str(text):
            assistant_speaks("Ok bye, "'.')
            quit()
        process_text(text)
def shutdown():
    assistant_speaks("shuting down your system do you want continue")
    ans = get_audio()
    if 'yes' in str(ans) or 'yeah' in str(ans):
     os.system('shutdown -s')

def process_text(input):
    try:
        if "who are you" in input or "define yourself" in input or "introduce yourself"in input:
            speak = '''Hello, I am Akira. Your personal Assistant.
            You can command me to perform various tasks such as calculating sums or opening applications'''
            assistant_speaks(speak)
            return
        elif "who made you" in input or "created you" in input:
            speak = "I have been created by vishnu sai."
            assistant_speaks(speak)
            return
        elif "hello" in input or "hi" in input:
            speak = "hello how can i help you."
            assistant_speaks(speak)
            return
        elif "hey Akira" in input or "Akira" in input or "akira"in input:
            speak = "what can i do for you."
            assistant_speaks(speak)
            return
        elif "time" in input or "created you" in input:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            assistant_speaks(f"Sir, the time is {strTime}")
            return
        elif "date" in input:
            strTime = datetime.datetime.now().strftime("%d:%m:%Y")
            assistant_speaks(f"Sir, the date is {strTime}")
            return
        elif 'send whatsapp message' in input:
            assistant_speaks("number to send whats up message")
            num = get_audio()
            if num:
                domain = num
                url = 'https://api.whatsapp.com/send?phone=91' + domain
                webbrowser.open(url)
                return
        elif "whats up" in input:
            assistant_speaks("whats up web")
            webbrowser.open("https://web.whatsapp.com/")
            return
        elif "calculate" in input.lower():
            app_id= "E46YXW-T5LG6RT7K7"
            client = wolframalpha.Client(app_id)

            indx = input.lower().split().index('calculate')
            query = input.split()[indx + 1:]
            res = client.query(' '.join(query))
            answer = next(res.results).text
            assistant_speaks("The answer is " + answer)
            return
        elif 'open' in input:
            open_application(input.lower())
            return
        elif 'Text mode' in input or "text mode" in input:
            speechtxt(input.lower())
            return
        elif 'play ' in input :
            youtube(input.lower())
            return
        elif 'amazon' in input :
            amazon(input.lower())
            return
        elif 'flipkart' in input :
            flipkart(input.lower())
            return
        elif 'swiggy' in input :
            swiggy(input.lower())
            return
        elif 'zomato' in input :
            zomato(input.lower())
            return
        elif 'search' in input:
            search(input.lower())
            return
        elif 'take photo' in input:
            TakeImages(input.lower())
            return
        elif 'weather' in input:
            weather(input.lower())
            return
        elif 'shutdown' in input:
            assistant_speaks("shuting down your system do you want continue")
            os.system('shutdown -s')
            return
        elif 'restart' in input:
            assistant_speaks("restart your system do you want continue")
            ans = get_audio()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                os.system('shutdown -r')
            return

        elif 'create folder' in input:
            florder(input.lower())
            return
        elif 'clean' in input:
            exist(input.lower())
            os.startfile("C:/Users/Public/clean.bat")
            os.startfile("C:/Users/Public/clean2.bat")
            os.popen('cleanmgr.exe /sagerun:1').read()
            assistant_speaks("system is cleaned")
            return
        elif 'mean' in input or "about"in input or "what" in input:
            wiki(input.lower())
            return
        elif 'close' in input or "Close"in input:
            close(input.lower())
            return
        elif 'hungry' in input or "place food order" in input:
            assistant_speaks("which service do you want to choose zomato or swiggy")
            ans = get_audio()
            if 'Zomato' in str(ans) or 'zomato' in str(ans):
                zito(input.lower())
            if 'swiggy' in str(ans) or 'swiggy' in str(ans):
                    swio(input.lower())
            return

        else:
            assistant_speaks("I can search the web for you, Do you want to continue?")
            ans = get_audio()
            if 'yes' in str(ans) or 'yeah' in str(ans):
                search(input.lower())
            else:
                return
    except Exception as e:
        print(e)
        assistant_speaks("I don't understand, I can search the web for you, Do you want to continue?")
        ans = get_audio()
        if 'yes' in str(ans) or 'yeah' in str(ans):
             search(input.lower())




def update(ind):
    frame = frames[(ind) % 100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)

frames = [PhotoImage(file='Assistant.gif', format='gif -index %i' % (i)) for i in range(100)]
window.title('JARVIS')

label = Label(window, width=500, height=500)
label.pack()
window.after(0, update, 0)

btn0 = Button(text='Akira', width=10, command=online, bg='#FAB60C')
btn0.config(font=("Courier", 12))
btn0.pack()
btn2 = Button(text='EXIT', width=20, command=window.destroy, bg='#5C85FB')
btn2.config(font=("Courier", 12))
btn2.pack()

if __name__ == "__main__":
        window.mainloop()