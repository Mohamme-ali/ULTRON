
import speech_recognition as sr
import pyttsx3
import keyboard
from time import sleep
import os
import pyautogui
import pywhatkit

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

        return "None"
    return query


# def HomeAutomation():

#     # try:
#     #     os.system('TASKKILL /F /im HD-Player.exe')
#     # except Exception as ex:
#     #     print(ex)

#     speak('Home Automation System Enabled')
#     keyboard.press_and_release('windows + s')
#     sleep(1)
#     keyboard.write('bluestack')
#     sleep(1)
#     keyboard.press('enter')
#     # speak('Please wait.')
#     sleep(1)
#     pyautogui.click(x=1544, y=172)
#     sleep(1)
#     # speak('Almost enabled')
#     pyautogui.click(x=1612, y=289)
#     # speak('Your requirement is fulfilled!!')
#     # speak('Please let me know how can I help you?')
#     pyautogui.click(x=1142, y=328)

def execute():

    def HomeAutomation():
        speak('Okay Mam!!')
        keyboard.press_and_release('windows + s')
        sleep(1)
        keyboard.write('bluestack')
        sleep(1)
        keyboard.press('enter')
        # speak('Please wait.')
        sleep(1)
        keyboard.press('f11')
        sleep(1)                 #
        pyautogui.click(x=1710, y=197)  # wipro app
        sleep(1)
        # speak('Almost enabled')
        pyautogui.click(x=1187, y=243)  # button
        sleep(2)
        keyboard.press('f11')
        sleep(1)
        pyautogui.click(x=1884, y=1000)  # home

        # speak('Your requirement is fulfilled!!')
        # speak('Please let me know how can I help you?')
        # pyautogui.click(x=1142, y=328)

    while True:
        order = takecommand()

        if 'on' in order:
            HomeAutomation()
            sleep(5)
        elif 'off' in order:
            HomeAutomation()
        elif 'colour' in order:
            speak("I'm changing the colour of the bulb.")
            # ChangeColor()
            sleep(5)
        elif 'brightness' in order:
            speak("Just a while!...... Done!!")
            sleep(5)
        elif 'music' in order:
            pywhatkit.playonyt("https://www.youtube.com/watch?v=fdubeMFwuGs")
            speak("Disco mode is turning on!! Meanwhile I'm Playing your playlist")
            keyboard.press('f')
            keyboard.press('l')
            keyboard.press('l')
            keyboard.press('l')

            sleep(50)
        elif 'bye' in order:
            speak("Okay!! Bye Bye")
            break
        else:
            speak('try again')
            break


execute()
