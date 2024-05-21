from suppress_errors import *
from agent import *
import time

nojackerr()
noalsaerr()

def main():
    wake_word = 'Jarvis'
    sleep_word = 'Goodbye'
    model_name = "google-deepmind/gemma-2b-it:dff94eaf770e1fc211e425a50b51baa8e4cac6c39ef074681f9e39d778773626"

    start = time.process_time()
    agent = Agent(wake_word=wake_word, sleep_word=sleep_word, model_name=model_name)
    agent.run()
    print(time.process_time() - start)

if __name__=="__main__":
    main()
