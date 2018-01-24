from connector import ev3

class speaker:
    def speak(text):
        if len(text) != 0:
            ev3.Sound.speak(text).wait()