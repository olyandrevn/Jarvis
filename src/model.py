import replicate

class LLM:
    def __init__(self, model_name):
        self.model_name = model_name

    def generate(self, input_text):
        print("Generating text...")

        output = replicate.run(
            self.model_name,
            input={
                "top_k": 50,
                "top_p": 0.95,
                "prompt": input_text,
                "temperature": 0.7,
                "max_new_tokens": 200,
                "min_new_tokens": -1,
                "repetition_penalty": 1.15
                }
        )
        generated_text = ''
        for item in output:
            generated_text += item

        return generated_text
