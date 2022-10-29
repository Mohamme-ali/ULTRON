
import speech_recognition as sr
import pyttsx3
import keyboard
from time import sleep
import os
import pyautogui

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
    keyboard.press('enter')
    speak('Please wait for some time.')
    sleep(55)
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


HomeAutomation()
