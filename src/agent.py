from speech2text import *
from text2speech import *
from model import *
from utils import *

class Agent:
    def __init__(self, wake_word, sleep_word, model_name=None, voice_recognition=True, voice_generation=True):
        if voice_recognition:
            self.stt = STT()
        if voice_generation:
            self.tts = TTS()
        if model_name:
            self.llm = LLM(model_name)

        self.wake_word = wake_word
        self.sleep_word = sleep_word
        self.voice_recognition = voice_recognition
        self.voice_generation = voice_generation
        self.model = (model_name != None)

    def get_input(self):
        if self.voice_recognition:
            text = self.stt.listen()
            print(f'You : {text}')
        else:
            text = input("You: ")

        return text

    def reply(self, text):
        if self.voice_generation:
            self.tts.speak(text)

        print(f'Jarvis : {text}')

    def run(self):
        intro = '''
        You can ask me:
        - open website x.com
        - what time is it?
        - to generate anything
        '''

        #self.reply(intro)

        if self.voice_recognition:
            print("Listening...")

        if self.wake_word in self.get_input():
            self.reply(intro)
            self.reply("What can I do for you, human?")
        else:
            return

        while True:
            input_text = self.get_input()
            if self.sleep_word in input_text:
                self.reply("Goodbye!")
                return

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
                    time = tell_time()
                    self.reply(f"The time is {time}.")
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

