from speech2text import *
from text2speech import *
from model import *
from utils import *
import time

class Agent:
    def __init__(self, wake_word, sleep_word, model_api=None, voice_recognition_api=None, voice_generation_api=None, speaker_name=None):
        if voice_recognition_api:
            self.stt = STT(voice_recognition_api)
        if voice_generation_api:
            self.tts = TTS(voice_generation_api, speaker_name)
        if model_api:
            self.llm = LLM(model_api)

        self.wake_word = wake_word
        self.sleep_word = sleep_word
        self.voice_recognition = voice_recognition_api is not None
        self.voice_generation = voice_generation_api is not None
        self.model = model_api is not None

    def get_input(self):
        if self.voice_recognition:
            start = time.process_time()

            text = self.stt.listen()

            print(f'You : {text}, {time.process_time() - start}')
        else:
            text = input("You: ")

        return text

    def reply(self, text):
        start = time.process_time()

        if self.voice_generation:
            self.tts.speak(text)

        print(f'Jarvis : {text}, {time.process_time() - start}')


    def run(self):
        if self.wake_word in self.get_input():
            self.reply("What can I do for you, human?")
        else:
            return

        while True:
            input_text = self.get_input()

            if self.sleep_word in input_text:
                self.reply("Goodbye!")
                return
            if not input_text.strip():
                print("No input detected. Waiting for input...")
                continue

            try:
                command = input_text.lower()

                if "open" in command:
                    if "website" in command:
                        url = command.split()[-1]
                        self.reply(f"Opening website {url}.")
                        open_website(url)
                    else:
                        self.reply("I'm not sure what you want me to open.")
                elif "time" in command:
                    ttime = tell_time()
                    self.reply(f"The time is {ttime}.")
                else:
                    if self.model:
                        generated_text = self.llm.generate(input_text)
                        self.reply(generated_text)
                    else:
                        self.reply("I'm sorry, I didn't understand that.")

            except sr.UnknownValueError:
                self.reply("I'm sorry, I didn't understand that.")
            except sr.RequestError as e:
                self.reply("Sorry, I couldn't reach the Google servers. Check your internet connection.")

