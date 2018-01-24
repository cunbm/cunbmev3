from utils import Utils
import speech_recognition as sr


class listener:

    def listen(noiseControl=0):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            if noiseControl != 0:
                print("Please wait. Calibrating microphone...")
                # listen for 3 seconds and create the ambient noise energy level
                r.adjust_for_ambient_noise(source, duration=noiseControl)
            print("You can now talk..")
            audio = r.listen(source)
        try:
            return r.recognize_bing(audio, Utils.bingApiKey)
        except sr.UnknownValueError:
            print(Utils.roboName, "could not understand audio")
        except sr.RequestError as e:
            print(Utils.roboName, "error; {0}".format(e))
