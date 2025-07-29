import subprocess

def read_code(file_path):
    """Reads the code from the specified file."""
    with open(file_path, 'r') as f:
        return f.read()

def run_code(code):
    """Executes the code and captures output and error logs."""
    try:
        # Write the code temporarily to a file to execute it
        with open("temp_script.py", "w") as f:
            f.write(code)

        # Execute the code and capture output and errors
        result = subprocess.run(
            ["python", "temp_script.py"],
            capture_output=True,
            text=True
        )

        # If exit code is 0, it means execution was successful
        if result.returncode == 0:
            return result.stdout, None  # Return output and no errors
        else:
            return result.stdout, result.stderr  # Return both output and errors

    except Exception as e:
        return None, str(e)  # In case of internal Python exceptions