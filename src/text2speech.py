import pyttsx3
import replicate
from playsound import playsound

class TTS:
    def __init__(self, api_name=None, speaker_name=None):
        self.engine = pyttsx3.init()
        self.api_name = api_name
        self.speaker_name = speaker_name 

    def speak(self, text):
        if self.api_name:
            print("Generating speech...")
            audio = replicate.run(
                self.api_name,
                input={
                    "text": text,
                    "speaker": self.speaker_name,
                    "language": "en",
                    "cleanup_voice": False
                }
            )
            playsound(audio)
        else:
            self.engine.say(text)
            self.engine.runAndWait()
