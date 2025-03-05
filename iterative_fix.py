from code_handler import read_code, run_code
from gpt4o_handler import call_gpt4o, create_prompt

def iterative_fix(file_path, purpose):
    for i in range(10):  # Limite massimo di iterazioni
        print(f"Iterazione {i + 1}...")

        # Leggere il codice dal file
        with open(file_path, 'r') as f:
            code = f.read()

        # Verificare con GPT-4o se il codice rispetta il purpose
        prompt = f"Does this code fulfill the purpose: {purpose}? \nHere is the code:\n{code}"
        confirmation = call_gpt4o(prompt)

        # Mostrare l'esecuzione del codice, indipendentemente dalla conformità
        print("Esecuzione del codice in corso...")
        output, error_log = run_code(code)
        print(f"Output del codice:\n{output}")
        if error_log:
            print(f"Errori del codice:\n{error_log}")

        # Se GPT-4o conferma che il codice rispetta il purpose
        if "yes" in confirmation.lower() and error_log is None:
            print("Il codice è conforme al purpose e non ci sono errori. Processo completato.")
            break
        else:
            print("Il codice non è conforme al purpose o ha generato errori. Richiedo correzioni.")

            # Chiediamo correzioni a GPT-4o
            prompt = create_prompt(code, error_log or confirmation, purpose)
            corrected_code = call_gpt4o(prompt)

            if corrected_code:
                # Aggiorna il file con il codice corretto
                with open(file_path, 'w') as f:
                    f.write(corrected_code)
                print(f"Codice aggiornato e salvato alla iterazione {i + 1}.")
            else:
                print(f"Nessuna correzione ricevuta all'iterazione {i + 1}.")
