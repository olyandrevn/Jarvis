from suppress_errors import *
from agent import Agent
import time

nojackerr()
noalsaerr()

def main():
    wake_word = 'Jarvis'
    sleep_word = 'Goodbye'
    model_api = "google-deepmind/gemma-2b-it:dff94eaf770e1fc211e425a50b51baa8e4cac6c39ef074681f9e39d778773626"
    voice_recognition_api = "openai/whisper:4d50797290df275329f202e48c76360b3f22b08d28c196cbc54600319435f8d2"
    voice_generation_api = "lucataco/xtts-v2:684bc3855b37866c0c65add2ff39c78f3dea3f4ff103a436465326e0f438d55e"
    speaker_name = "https://replicate.delivery/pbxt/Jt79w0xsT64R1JsiJ0LQRL8UcWspg5J4RFrU6YwEKpOT1ukS/male.wav"

    start = time.process_time()

    agent = Agent(wake_word,
                  sleep_word,
                  model_api,
                  voice_recognition_api,
                  voice_generation_api,
                  speaker_name)
    agent.run()
    print(time.process_time() - start)

if __name__=="__main__":
    main()
