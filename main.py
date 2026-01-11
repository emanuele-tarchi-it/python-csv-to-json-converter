__version__ = "1.1.0"
__author__ = "Emanuele Tarchi"

import pandas as pd
import json
import os
import tkinter as tk
from tkinter import filedialog, messagebox

def csv_to_json_logic(input_file, output_file, indent=2):
    """Logica pura di conversione (il tuo motore)"""
    try:
        df = pd.read_csv(input_file)
        data = df.to_dict(orient="records")
        with open(output_file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=indent, ensure_ascii=False)
        return True, len(data)
    except Exception as e:
        return False, str(e)

def avvia_processo():
    """Gestisce l'interazione con l'utente tramite finestre"""
    # 1. Seleziona il file sorgente
    file_sorgente = filedialog.askopenfilename(
        title="Seleziona il file CSV",
        filetypes=[("Documenti CSV", "*.csv")]
    )
    
    if not file_sorgente:
        return # L'utente ha chiuso la finestra senza scegliere

    # 2. Chiedi dove salvare il risultato
    file_destinazione = filedialog.asksaveasfilename(
        title="Salva il file JSON come...",
        defaultextension=".json",
        filetypes=[("File JSON", "*.json")]
    )

    if not file_destinazione:
        return

    # 3. Esegui la conversione usando la logica definita sopra
    successo, risultato = csv_to_json_logic(file_sorgente, file_destinazione)

    # 4. Feedback all'utente
    if successo:
        messagebox.showinfo("Successo!", f"Conversione completata.\nRecord convertiti: {risultato}")
    else:
        messagebox.showerror("Errore", f"Si è verificato un problema:\n{risultato}")

# --- SETUP DELLA GUI ---
def crea_interfaccia():
    root = tk.Tk()
    root.title("Tarchi CSV to JSON Converter")
    root.geometry("400x200")
    
    # Etichetta di benvenuto
    label = tk.Label(root, text="Convertitore Professionale CSV", font=("Arial", 12, "bold"))
    label.pack(pady=20)

    # Bottone principale
    btn = tk.Button(
        root, 
        text="Sfoglia e Converti", 
        command=avvia_processo,
        bg="#2ecc71", # Un bel verde "successo"
        fg="white",
        font=("Arial", 10, "bold"),
        padx=20,
        pady=10
    )
    btn.pack(pady=10)

    # Footer
    footer = tk.Label(root, text=f"v{__version__} | {__author__}", fg="gray")
    footer.pack(side="bottom", pady=10)

    root.mainloop()

if __name__ == "__main__":
    crea_interfaccia()
