from code_handler import read_code, run_code
from gpt4o_handler import call_gpt4o, create_prompt

def iterative_fix(file_path, purpose):
    for i in range(10):  # Maximum iteration limit
        print(f"Iteration {i + 1}...")

        # Read the code from the file
        with open(file_path, 'r') as f:
            code = f.read()

        # Check with GPT-4o if the code fulfills the purpose
        prompt = f"Does this code fulfill the purpose: {purpose}? \nHere is the code:\n{code}"
        confirmation = call_gpt4o(prompt)

        # Show code execution regardless of compliance
        print("Code execution in progress...")
        output, error_log = run_code(code)
        print(f"Code output:\n{output}")
        if error_log:
            print(f"Code errors:\n{error_log}")

        # If GPT-4o confirms that the code fulfills the purpose
        if "yes" in confirmation.lower() and error_log is None:
            print("Code is compliant with the purpose and has no errors. Process completed.")
            break
        else:
            print("Code is not compliant with the purpose or has generated errors. Requesting corrections.")

            # Request corrections from GPT-4o
            prompt = create_prompt(code, error_log or confirmation, purpose)
            corrected_code = call_gpt4o(prompt)

            if corrected_code:
                # Update the file with the corrected code
                with open(file_path, 'w') as f:
                    f.write(corrected_code)
                print(f"Code updated and saved at iteration {i + 1}.")
            else:
                print(f"No correction received at iteration {i + 1}.")