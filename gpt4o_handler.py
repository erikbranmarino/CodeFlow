import openai
import re

# Set your OpenAI API key (for testing, but store securely in production)
openai.api_key = "xxx"

def extract_code(response_text):
    """Extract Python code enclosed in triple backticks."""
    code_blocks = re.findall(r"```python(.*?)```", response_text, re.DOTALL)
    if code_blocks:
        return code_blocks[0].strip()  # Extract the first block of Python code
    else:
        return response_text.strip()  # Return the whole response if no code block is found

def call_gpt4o(prompt):
    """Send the prompt to GPT-4o and receive the correction for the code."""
    try:
        # Correct usage for OpenAI SDK v1.x
        response = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are an expert Python developer."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1500
        )

        # Correct way to access the response in the new API
        raw_response = response['choices'][0]['message']['content']
        return extract_code(raw_response)  # Extract only the Python code
    except Exception as e:
        print(f"Error with OpenAI API call: {e}")
        return None

def create_prompt(code, error_log, purpose):
    """Crea un prompt per GPT-4o che richiede solo la correzione del codice."""
    return f"""
    You are an expert Python developer. The goal of this script is: {purpose}.

    Here is the current version of the Python code:

    {code}

    It generated the following result:

    {error_log}

    Please fix the error and provide ONLY the corrected complete Python code. 
    Do not include any explanation, comments, pip install or additional text, just the code itself. 
    JUST THE CODE. NO HEADERS, NOTHING MORE THAN THE CODE. NOT EVEN: "```Python" at the beginning or at the end "```".
    """

