import speech_recognition as sr
import replicate
import base64
import time

class STT:
    def __init__(self, api_name=None):
        self.engine = sr.Recognizer()
        self.engine.pause_threshold = 1
        self.api_name = api_name

    def listen(self):
        with sr.Microphone() as source:
            print("Listening...")
            audio = self.engine.listen(source)
            time.sleep(2)

        if self.api_name: 
            with open("in.wav", "wb") as f:
                f.write(audio.get_wav_data())

            print("Transcribing...")
            with open("in.wav", 'rb') as file:
                data = base64.b64encode(file.read()).decode('utf-8')
                audio = f"data:application/octet-stream;base64,{data}"

            transcribtion = replicate.run(
                self.api_name,
                input={
                    "audio": audio,
                    "language": "en",
                    "model": "large-v3",
                }
            )
            return transcribtion['transcription']

        else:
            text = self.engine.recognize_whisper(audio)
            return text
