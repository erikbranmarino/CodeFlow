import subprocess

def read_code(file_path):
    """Legge il codice dal file specificato."""
    with open(file_path, 'r') as f:
        return f.read()

def run_code(code):
    """Esegue il codice e cattura l'output e il log degli errori."""
    try:
        # Scriviamo il codice temporaneamente in un file per eseguirlo
        with open("temp_script.py", "w") as f:
            f.write(code)

        # Eseguiamo il codice e catturiamo l'output e gli errori
        result = subprocess.run(
            ["python", "temp_script.py"],
            capture_output=True,
            text=True
        )

        # Se l'exit code è 0, significa che l'esecuzione è andata a buon fine
        if result.returncode == 0:
            return result.stdout, None  # Restituiamo l'output e nessun errore
        else:
            return result.stdout, result.stderr  # Restituiamo sia l'output che gli errori

    except Exception as e:
        return None, str(e)  # In caso di eccezioni Python interne
