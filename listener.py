from utils import Utils
import speech_recognition as sr


class listener:
    def __init__(self, name, noiseControl= 3):
        self.name = name
        self.noiseControl = noiseControl
        self.r = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            print("Please wait. Calibrating microphone...")
            # listen for 3 seconds and create the ambient noise energy level
            self.r.adjust_for_ambient_noise(source, duration=self.noiseControl)
            audio = self.r.listen(source)

        try:
            print("'" + self.r.recognize_bing(audio, Utils.bingApiKey) + "'")
        except sr.UnknownValueError:
            print(Utils.roboName, "could not understand audio")
        except sr.RequestError as e:
            print(Utils.roboName, "error; {0}".format(e))


