import os
from iterative_fix import iterative_fix


def read_purpose(file_path):
    """Reads the content of the purpose file and returns it as a string."""
    with open(file_path, 'r') as file:
        return file.read().strip()


def main():
    purpose_file_path = 'purpose'  # Path to the "purpose" file

    # Read the purpose from the "purpose" file
    purpose = read_purpose(purpose_file_path)

    # Path to the code file to be fixed
    file_path = 'script.py'

    # Execute the iteration with the read purpose
    iterative_fix(file_path, purpose)


if __name__ == "__main__":
    main()