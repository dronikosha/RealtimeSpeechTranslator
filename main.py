import threading

import pyttsx3
import speech_recognition as sr
from googletrans import Translator, constants
from speech_recognition import UnknownValueError

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(u"Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(
        index, name))

r = sr.Recognizer()



def speech_recorder():
    try:
        while True:
            with sr.Microphone(device_index=1) as source:
                engine = pyttsx3.init()
                print("1")
                r.adjust_for_ambient_noise(source=source)
                audio = r.listen(source)
                text = r.recognize_google(audio, language="ru-RU")
                translator = Translator().translate(text=text, dest="en")
                print(translator.text)
                print("2")
                engine.say(translator.text)
                engine.runAndWait()
                engine.stop()
                print("3")
                if "стоп" in text:
                    break
                text = None
                audio = None
    except UnknownValueError:
        print("4")
        speech_recorder()


recorder_thread = threading.Thread(target=speech_recorder)
recorder_thread.start()
# recognizer_thread = threading.Thread(target=recognizer, args=speech_recorder)
# recognizer_thread.start()


print("SPEAK")
