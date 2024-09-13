import math
import tkinter as tk
from tkinter import messagebox, font
import time

class TrapezioIsosceleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tool Trapezio Isoscele")
        self.root.geometry("400x400")
        self.root.minsize(300, 300)
        self.root.configure(bg="#F5F5F5")

        # Font e stili
        self.font_title = font.Font(family="Segoe UI", size=16, weight="bold")
        self.font_labels = font.Font(family="Segoe UI", size=12)
        self.font_button = font.Font(family="Segoe UI", size=12, weight="bold")
        self.font_result = font.Font(family="Segoe UI", size=12)
        self.font_error = font.Font(family="Segoe UI", size=12, weight="bold")

        # Etichetta per il logo in ASCII art
        self.label_logo = tk.Label(root, text=self.get_logo(), font=("Courier New", 10, "bold"), bg="#F5F5F5", anchor="w", justify="left", padx=10, pady=10, fg="#0056A0")
        self.label_logo.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        # Titolo dell'app
        self.label_title = tk.Label(root, text="Calcolatrice Trapezio", font=self.font_title, bg="#F5F5F5", fg="#343A40")
        self.label_title.grid(row=1, column=0, columnspan=2, pady=10)

        # Creazione di un frame per gli input
        self.frame_inputs = tk.Frame(root, bg="#FFFFFF", padx=10, pady=10, borderwidth=2, relief="flat")
        self.frame_inputs.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Etichette e campi di input
        self.label_base_maggiore = tk.Label(self.frame_inputs, text="Base maggiore (B):", font=self.font_labels, bg="#FFFFFF", fg="#FF6F00")
        self.label_base_maggiore.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_base_maggiore = tk.Entry(self.frame_inputs, font=self.font_labels, width=20, borderwidth=1, relief="solid")
        self.entry_base_maggiore.grid(row=0, column=1, padx=5, pady=5)

        self.label_base_minore = tk.Label(self.frame_inputs, text="Base minore (b):", font=self.font_labels, bg="#FFFFFF", fg="#FF6F00")
        self.label_base_minore.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_base_minore = tk.Entry(self.frame_inputs, font=self.font_labels, width=20, borderwidth=1, relief="solid")
        self.entry_base_minore.grid(row=1, column=1, padx=5, pady=5)

        self.label_altezza = tk.Label(self.frame_inputs, text="Altezza (h):", font=self.font_labels, bg="#FFFFFF", fg="#FF6F00")
        self.label_altezza.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_altezza = tk.Entry(self.frame_inputs, font=self.font_labels, width=20, borderwidth=1, relief="solid")
        self.entry_altezza.grid(row=2, column=1, padx=5, pady=5)

        # Pulsante per calcolare area e perimetro
        self.button_calcola = tk.Button(root, text="Calcola", font=self.font_button, bg="#007ACC", fg="white", activebackground="#005999", activeforeground="white", command=self.calcola, relief="raised", borderwidth=1)
        self.button_calcola.grid(row=3, column=0, columnspan=2, pady=10)

        # Etichetta per il risultato
        self.label_risultato = tk.Label(root, text="", font=self.font_result, bg="#F5F5F5", fg="#0056A0", wraplength=350)
        self.label_risultato.grid(row=4, column=0, columnspan=2, pady=10)

        # Crediti in fondo
        self.label_crediti = tk.Label(root, text="Sviluppato da Leo - 2024", font=self.font_error, bg="#F5F5F5", fg="#6C757D")
        self.label_crediti.grid(row=5, column=0, columnspan=2, pady=10)

        # Espandere il frame degli input
        root.grid_rowconfigure(2, weight=1)
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=1)

    def get_logo(self):
        return (
            "████████╗██████╗  █████╗ ██████╗ ███████╗███████╗██╗ ██████╗ \n"
            "╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══███╔╝██║██╔═══██╗\n"
            "   ██║   ██████╔╝███████║██████╔╝█████╗    ███╔╝ ██║██║   ██║\n"
            "   ██║   ██╔══██╗██╔══██║██╔═══╝ ██╔══╝   ███╔╝  ██║██║   ██║\n"
            "   ██║   ██║  ██║██║  ██║██║     ███████╗███████╗██║╚██████╔╝\n"
            "   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚══════╝╚═╝ ╚═════╝ \n"
        )

    def calcola(self):
        try:
            # Recupera i valori inseriti
            base_maggiore = float(self.entry_base_maggiore.get())
            base_minore = float(self.entry_base_minore.get())
            altezza = float(self.entry_altezza.get())

            # Controllo se le basi sono valide
            if base_maggiore <= base_minore:
                self.show_error("La base maggiore deve essere maggiore della base minore.")
                return

            # Inizio misurazione tempo
            start_time = time.time()

            # Calcolo area e perimetro
            area = self.calcola_area(base_maggiore, base_minore, altezza)
            perimetro = self.calcola_perimetro(base_maggiore, base_minore, altezza)

            # Fine misurazione tempo
            end_time = time.time()

            # Calcolo tempo impiegato in millisecondi
            tempo_impiegato = (end_time - start_time) * 1000

            # Mostra i risultati
            risultato = f"Area: {area:.2f} metri quadrati\nPerimetro: {perimetro:.2f} metri\nTempo impiegato: {tempo_impiegato:.2f} ms"
            self.label_risultato.config(text=risultato, fg="#0056A0")

        except ValueError:
            self.show_error("Inserisci valori numerici validi.")

    def show_error(self, message):
        messagebox.showerror("Errore", message)
        self.label_risultato.config(text=message, fg="#FF4C4C")

    def calcola_area(self, base_maggiore, base_minore, altezza):
        return ((base_maggiore + base_minore) * altezza) / 2

    def calcola_perimetro(self, base_maggiore, base_minore, altezza):
        lato_obliquo = math.sqrt(((base_maggiore - base_minore) ** 2) / 4 + altezza ** 2)
        return base_maggiore + base_minore + 2 * lato_obliquo

if __name__ == "__main__":
    root = tk.Tk()
    app = TrapezioIsosceleApp(root)
    root.mainloop()
