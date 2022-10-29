# pip install pyttsx3
# pip install SpeechRecognition
# pip install pyautogui
# pip install pywhatkit
# pip install keyboard
# pip install pyjokes
# pip install PyDictionary
# pip install pydictionary
# pip install playsound

# pip list  == to check list of all modulesg

# google search with no url provided    # whatsapp message       # play on youtube
import pywhatkit
import speech_recognition as sr  # to let the system hear us
import pyttsx3  # to add voice
import webbrowser  # to search somthing on web
import os       # to let the assistant open app or something
import wikipedia
import pyautogui  # screenshot#
import keyboard  # to press keyboard keys
import pyjokes    # to hear jokes
from PyDictionary import PyDictionary
import datetime
from playsound import playsound
from time import sleep


# audio of system to respond
ultron = pyttsx3.init('sapi5')
voices = ultron.getProperty('voices')
# print(voices)
ultron.setProperty('voice', voices[1].id)
ultron.setProperty('rate', 170)


def speak(audio):
    ultron.say(audio)
    print(f"✔ {audio}")
    print("    ")
    ultron.runAndWait()


# speak('Hello Paarth')
# speak('')
# simple function to recognise speech from user
# it takes microphone input and returns string output


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening.....')
        r.pause_threshold = 1
        r.energy_threshold = 4000
        audio = r.listen(source)

    try:
        print('Recognising...')
        query = r.recognize_google(audio, language='en-in')
        print('You Said : ', query)

    except Exception as e:
        print('exception : ', e)

        # speak("Sorry, I didn't hear that, Say that again Please")
        return "None"
    return query


def taskExecution():
    speak("Ultron is Waking Up!!")

    def playMusic():
        speak("Tell me the name of song")
        name = takecommand()
        if 'abc' in name:
            os.startfile('C:\\songs\\abc.mp3')
        else:
            pywhatkit.playonyt(name)

        speak("Your song is going to start soon.")

    def startapp():
        speak("Okay..Which app do you want to open?")
        app = takecommand()
        speak("Okay Sir... Opening the application")
        if 'code' in app:
            os.startfile(
                "C:\\Microsoft VS Code\\Code.exe")
        elif 'WhatsApp' in app:
            os.startfile(
                "C:\\Users\\Dell\\AppData\\Local\\WhatsApp\\WhatsApp.exe")

        elif 'player' in app:
            os.startfile("C:\\Program Files\\VideoLAN\\VLC\\vlc.exe")

        elif 'Maps' in app:
            webbrowser.open(
                "https://www.google.co.in/maps/place/Nirwana+Greens+4/@30.7481499,76.6437874,14z/data=!4m5!3m4!1s0x390ffba53253b851:0xb9e8492f403be9e5!8m2!3d30.7629154!4d76.6284448")
        else:
            speak("I'm Sorry.. I cant find the application")
        speak("I hope this is what you were looking for!!")

    def CloseAPP():
        speak("Which app do you want to Close?")
        app = takecommand()
        if 'WhatsApp' in app:
            os.system("TASKKILL /F /im WhatsApp.exe")
        else:
            speak("Unable to find the application")
        speak("Closed Successfully!")

    def WhatsApp():
        speak("Whom do you want to message?")
        person = takecommand()
        if 'my number' in person:
            speak("What is the message?")
            mess = takecommand()
            speak("Now, tell me time at which you want to sen message")
            speak("Hour?")
            hr = int(takecommand())
            speak("Minute?")
            min = int(takecommand())
            pywhatkit.sendwhatmsg("+91 7069817634", mess, hr, min, 20)
            speak("Okay..I'm Sending the whatsapp message")

        else:
            speak("Tell me the phone number")
            phnum = int(takecommand())
            number = '+91' + phnum
            speak("What is the message?")
            mess = takecommand()
            speak("Now, tell me time at which you want to sen message")
            speak("Hour?")
            hr = int(takecommand())
            speak("Minute?")
            min = int(takecommand())
            pywhatkit.sendwhatmsg(number, mess, hr, min, 20)
            speak("Okay..I'm Sending the whatsapp message")

    def YouAuto():
        speak("What's your command?")
        while True:
            command = takecommand()
            if 'pause' in command:
                keyboard.press('space bar')
            elif 'mute' in command:
                keyboard.press('m')
            elif 'restart' in command:
                keyboard.press('0')
            elif 'forward' in command:
                keyboard.press('l')
            elif 'back' in command:
                keyboard.press('j')
            elif 'full screen' in command:
                keyboard.press('f')
            elif 'film ' in command:
                keyboard.press('t')
            elif 'close' in command:
                os.system("TASKKILL /F /im chrome.exe")
                speak("Done Sir")
                break

    def Dictionaryy():
        speak("Enabled")
        speak("What is the word?")
        word = takecommand()
        dict = PyDictionary(word, 2)
        answer = dict.meanings()
        # answer = Dictionary.meanings(word)
        speak(f"Meaning of {word} is {answer}")

    def SetAlarm():
        speak("Enter the Time")
        time = input("(Format = H:M:S)👀 Enter:  ")
        while True:
            Timee = datetime.datetime.now()
            noww = Timee.strftime("%H:%M:%S")

            if noww == time:
                speak("It's Time to Wake Up")
                playsound(
                    'c:\\SEM6-SM\\Minor Project\\Project\\ULTRON\\basics\\play.mp3')

            elif noww > time:
                break

    def HomeAutomation():
        try:
            os.system('TASKKILL /F /im HD-Player.exe')
        except Exception as ex:
            print(ex)

        speak('Home Automation System Enabled')
        keyboard.press_and_release('windows + s')
        sleep(1)
        keyboard.write('bluestack')
        sleep(1)
        speak('Please wait for some time.')
        keyboard.press('enter')
        sleep(30)
        pyautogui.click(x=1554, y=188)
        sleep(5)
        speak('Almost enabled')
        pyautogui.click(x=1606, y=283)
        sleep(20)
        speak('Your requirement is fulfilled!!')
        speak('Please let me know how can I help you?')
        while True:
            cmnd = takecommand()
            if 'off' in cmnd:
                pyautogui.click(x=1142, y=328)
            elif 'on' in cmnd:
                pyautogui.click(x=1142, y=328)
            else:
                break

    while True:

        query = takecommand()

        if 'hello' in query:
            speak('Hello Sir! Ultron is in your service now! What can I do for You?')

        elif 'how are you' in query:
            speak("I'm good and ready to serve you")

        elif 'bye bye' in query:
            speak("Ok Sir! Bye Bye.. You can call me anytime!")
            break

        elif 'YouTube search' in query:
            speak('Okay....')
            query = query.replace("OK", "")
            query = query.replace("Ultron", "")
            query = query.replace("YouTube search", "")
            web = 'https://www.youtube.com/results?search_query=' + query
            webbrowser.open(web)
            speak(
                'Check it outt!!')
            speak("Do you want to enable Youtube automation feature?")
            ans = takecommand()
            if 'yes' in ans:
                YouAuto()
            else:
                continue

        elif 'Google search' in query:
            speak('Okay...')
            query = query.replace("OK", "")
            query = query.replace("Ultron", "")
            query = query.replace("Google search", "")
            pywhatkit.search(query)
            speak(
                'This is what I found on Google.. I hope this is what you were looking for!!')

        elif 'open website' in query:
            speak('Okay...')
            query = query.replace("OK", "")
            query = query.replace("Ultron", "")
            query = query.replace("open", "")
            query = query.replace("website", "")

            web2 = 'https://www.'+query+'.com'
            # print(web2)
            web1 = "".join(web2.split())
            web3 = web1.lower()
            # print(web3)
            webbrowser.open(web3)
            speak(
                'This is what I found on Google.. I hope this is what you were looking for!!')

        elif 'music' in query:
            playMusic()

        elif 'Wikipedia' in query:
            speak("Searching in Wikipedia..")
            query = query.replace("search", "")
            query = query.replace("on", "")
            query = query.replace("Wikipedia", "")
            # try saying "search iot on wikipedia"
            print(query)
            searchit = wikipedia.summary(query, 1)
            speak(f"According to wikipedia {searchit}")

        elif 'screenshot' in query:
            speak("Ok..By what name would you like to save it?")
            location = takecommand()
            loc = location+'.png'
            path = "c:\\Users\\DELL\\Desktop\\Screenshots\\"+loc
            ss = pyautogui.screenshot()
            ss.save(path)
            speak("Saved Sucessfully ")
            speak("You wanna see that Screenshot?")
            opinion = takecommand()
            if 'yes' in opinion:
                os.startfile(
                    f"c:\\Users\\DELL\\Desktop\\Screenshots\\{loc}")
            else:
                speak("Okayy!!")

        elif 'open app' in query:
            startapp()

        elif 'WhatsApp message' in query:
            WhatsApp()

        elif 'close app' in query:
            CloseAPP()

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'monkey game' in query:
            speak("Okay!! Let's get started!!")
            while True:
                word = takecommand()
                if 'stop it' in word:
                    speak("Okay Sir! Game Ended!")
                    break
                else:
                    speak(word)

        elif 'location' in query:
            webbrowser.open(
                "https://www.google.co.in/maps/place/Nirwana+Greens+4/@30.7481499,76.6437874,14z/data=!4m5!3m4!1s0x390ffba53253b851:0xb9e8492f403be9e5!8m2!3d30.7629154!4d76.6284448")

        elif 'dictionary' in query:
            Dictionaryy()

        elif 'alarm' in query:
            SetAlarm()

        elif 'Home Automation' in query:
            HomeAutomation()

        else:
            speak("Try again..")


taskExecution()
