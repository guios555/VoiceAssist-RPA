import pyttsx3


class Speaker:

    def __init__(self):
        self.engine = pyttsx3.init()
        self.engine.setProperty("rate", 175)
        self.engine.setProperty("volume", 1.0)

    def speak(self, message):
        print(f"Wúai: {message}")

        self.engine.say(message)
        self.engine.runAndWait()