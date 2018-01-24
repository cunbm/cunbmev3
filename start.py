# from connector import ev3
#
# m = ev3.LargeMotor()
# m.run_timed(time_sp=3000, speed_sp=1000)
from utils import Utils
import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Please wait. Calibrating microphone...")
    # listen for 3 seconds and create the ambient noise energy level
    r.adjust_for_ambient_noise(source, duration=3)
    print("Say something!")
    audio = r.listen(source)

    # recognize speech using Sphinx
try:
    print("'" + r.recognize_bing(audio, Utils.bingApiKey) + "'")
except sr.UnknownValueError:
    print("Sphinx could not understand audio")
except sr.RequestError as e:
    print("Sphinx error; {0}".format(e))
