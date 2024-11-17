import openai
import pandas as pd
import re
import builtins
import io

# Initialize OpenAI with API key
openai.api_key = 'openai-api-key'

def call_openai(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
        temperature=0.5
    )
    return response.choices[0].text.strip()

class CustomLangChainAgent:
    def __init__(self, api_key: str):
        openai.api_key = api_key

    def generate_code(self, prompt: str) -> str:
        instruction_template = f"""
        You are a Python developer. Write code to perform the following task:
        Task: "{prompt}"
        Ensure the code is properly formatted, sanitized, and free of unsafe operations.
        """
        return call_openai(instruction_template)

    def execute_code(self, code: str, context: dict) -> str:
        # Secure execution context
        safe_builtins = {k: getattr(builtins, k) for k in dir(builtins) if not k.startswith('__')}
        exec_context = {
            'pd': pd,
            **safe_builtins,
            **context
        }

        try:
            stdout = io.StringIO()
            exec(code, exec_context)
            return stdout.getvalue()
        except Exception as e:
            return str(e)

    def process_prompt(self, prompt: str, data=None) -> str:
        generated_code = self.generate_code(prompt)
        print("Generated Code:")
        print(generated_code)
        return self.execute_code(generated_code, {'data': data})

if __name__ == "__main__":
    API_KEY = 'openai-api-key'
    agent = CustomLangChainAgent(api_key=API_KEY)

    user_prompt = "Calculate the average value of a column named 'age' in the provided dataframe."

    sample_data = pd.DataFrame({'age': [23, 45, 35, 67, 34]})

    try:
        result = agent.process_prompt(user_prompt, data=sample_data)
        print("Execution Result:")
        print(result)
    except Exception as e:
        print("An error occurred:")
        print(e)