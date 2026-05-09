import pyttsx3

class Say:
    def __init__(self,speach,voice_id):
        self.string = speach
        self.vosBool = int(voice_id)

    def sayLoud(self):
        engine = pyttsx3.init()
        engine.stop()
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[self.vosBool].id)
        engine.say(self.string)
        engine.runAndWait()

