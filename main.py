import os
from iterative_fix import iterative_fix


def read_purpose(file_path):
    """Legge il contenuto del file purpose e lo restituisce come stringa."""
    with open(file_path, 'r') as file:
        return file.read().strip()


def main():
    purpose_file_path = 'purpose'  # Percorso del file "purpose"

    # Leggere lo scopo dal file "purpose"
    purpose = read_purpose(purpose_file_path)

    # Percorso del file di codice da correggere
    file_path = 'script.py'

    # Eseguire l'iterazione con il purpose letto
    iterative_fix(file_path, purpose)


if __name__ == "__main__":
    main()
