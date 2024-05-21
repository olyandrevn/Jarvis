import speech_recognition as sr
import whisper
import replicate

class STT:
    def __init__(self):
        self.engine = sr.Recognizer()
        self.engine.pause_threshold = 1

    def listen(self):
        with sr.Microphone() as source:
            audio = self.engine.listen(source)

        text = self.engine.recognize_whisper(audio)
        return text
