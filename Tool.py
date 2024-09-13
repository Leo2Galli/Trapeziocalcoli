import math
import tkinter as tk
from tkinter import messagebox, font
from tkinter import ttk
import time
import matplotlib.pyplot as plt
import numpy as np

class TrapezioIsosceleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calcolo Trapezio Simmetrico")
        self.root.geometry("500x500")
        self.root.minsize(400, 400)
        self.root.configure(bg="#F5F5F5")

        # Font e stili
        self.font_title = font.Font(family="Segoe UI", size=16, weight="bold")
        self.font_labels = font.Font(family="Segoe UI", size=12)
        self.font_button = font.Font(family="Segoe UI", size=12, weight="bold")
        self.font_result = font.Font(family="Segoe UI", size=12)
        self.font_error = font.Font(family="Segoe UI", size=12, weight="bold")

        # Dizionario delle traduzioni
        self.translations = {
            "italiano": {
                "title": "Calcolatrice Trapezio Simmetrico",
                "base_maggiore": "Base maggiore (B):",
                "base_minore": "Base minore (b):",
                "altezza": "Altezza (h):",
                "calculate": "Calcola",
                "formula_title": "Formule",
                "graph_title": "Grafico Trapezio Isoscele Simmetrico",
                "figure_title": "Figura 1",
                "error_base": "La base maggiore deve essere maggiore della base minore.",
                "error_value": "Inserisci valori numerici validi.",
                "formula_text": "Area = ((B + b) * h) / 2\nPerimetro = B + b + 2 * lato obliquo\nDove lato obliquo = sqrt(((B - b) / 2) ** 2 + h ** 2)"
            },
            "english": {
                "title": "Isosceles Trapezoid Calculator",
                "base_maggiore": "Major base (B):",
                "base_minore": "Minor base (b):",
                "altezza": "Height (h):",
                "calculate": "Calculate",
                "formula_title": "Formulas",
                "graph_title": "Isosceles Trapezoid Graph",
                "figure_title": "Figure 1",
                "error_base": "The major base must be greater than the minor base.",
                "error_value": "Please enter valid numeric values.",
                "formula_text": "Area = ((B + b) * h) / 2\nPerimeter = B + b + 2 * slant height\nWhere slant height = sqrt(((B - b) / 2) ** 2 + h ** 2)"
            },
            "deutch": {
                "title": "Symmetrisches Trapez Rechner",
                "base_maggiore": "Größere Basis (B):",
                "base_minore": "Kleinere Basis (b):",
                "altezza": "Höhe (h):",
                "calculate": "Berechnen",
                "formula_title": "Formeln",
                "graph_title": "Symmetrisches Trapez Diagramm",
                "figure_title": "Abbildung 1",
                "error_base": "Die größere Basis muss größer als die kleinere Basis sein.",
                "error_value": "Bitte geben Sie gültige numerische Werte ein.",
                "formula_text": "Fläche = ((B + b) * h) / 2\nUmfang = B + b + 2 * Schenkelhöhe\nWobei Schenkelhöhe = sqrt(((B - b) / 2) ** 2 + h ** 2)"
            },
            "Español": {
                "title": "Calculadora de Trapecio Isósceles",
                "base_maggiore": "Base mayor (B):",
                "base_minore": "Base menor (b):",
                "altezza": "Altura (h):",
                "calculate": "Calcular",
                "formula_title": "Fórmulas",
                "graph_title": "Gráfico de Trapecio Isósceles",
                "figure_title": "Figura 1",
                "error_base": "La base mayor debe ser mayor que la base menor.",
                "error_value": "Por favor, ingrese valores numéricos válidos.",
                "formula_text": "Área = ((B + b) * h) / 2\nPerímetro = B + b + 2 * altura inclinada\nDonde altura inclinada = sqrt(((B - b) / 2) ** 2 + h ** 2)"
            },
            "中国人": {
                "title": "等腰梯形计算器",
                "base_maggiore": "大底边 (B):",
                "base_minore": "小底边 (b):",
                "altezza": "高度 (h):",
                "calculate": "计算",
                "formula_title": "公式",
                "graph_title": "等腰梯形图",
                "figure_title": "图 1",
                "error_base": "大底边必须大于小底边。",
                "error_value": "请输入有效的数值。",
                "formula_text": "面积 = ((B + b) * h) / 2\n周长 = B + b + 2 * 斜边\n其中斜边 = sqrt(((B - b) / 2) ** 2 + h ** 2)"
            }
        }

        self.current_language = "italiano"

        # Etichetta per il logo
        self.label_logo = tk.Label(root, text=self.get_logo(), font=("Courier New", 10, "bold"), bg="#F5F5F5", anchor="w", justify="left", padx=10, pady=10, fg="#0056A0")
        self.label_logo.grid(row=0, column=0, columnspan=2, padx=10, pady=5, sticky="w")

        # Titolo dell'app
        self.label_title = tk.Label(root, text=self.translations[self.current_language]["title"], font=self.font_title, bg="#F5F5F5", fg="#343A40")
        self.label_title.grid(row=1, column=0, columnspan=2, pady=10)

        # Creazione di un frame per gli input
        self.frame_inputs = tk.Frame(root, bg="#FFFFFF", padx=10, pady=10, borderwidth=2, relief="flat")
        self.frame_inputs.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Etichette e campi di input
        self.label_base_maggiore = tk.Label(self.frame_inputs, text=self.translations[self.current_language]["base_maggiore"], font=self.font_labels, bg="#FFFFFF", fg="#333333")
        self.label_base_maggiore.grid(row=0, column=0, padx=5, pady=5, sticky="e")
        self.entry_base_maggiore = tk.Entry(self.frame_inputs, font=self.font_labels, width=20, borderwidth=1, relief="solid")
        self.entry_base_maggiore.grid(row=0, column=1, padx=5, pady=5)

        self.label_base_minore = tk.Label(self.frame_inputs, text=self.translations[self.current_language]["base_minore"], font=self.font_labels, bg="#FFFFFF", fg="#333333")
        self.label_base_minore.grid(row=1, column=0, padx=5, pady=5, sticky="e")
        self.entry_base_minore = tk.Entry(self.frame_inputs, font=self.font_labels, width=20, borderwidth=1, relief="solid")
        self.entry_base_minore.grid(row=1, column=1, padx=5, pady=5)

        self.label_altezza = tk.Label(self.frame_inputs, text=self.translations[self.current_language]["altezza"], font=self.font_labels, bg="#FFFFFF", fg="#333333")
        self.label_altezza.grid(row=2, column=0, padx=5, pady=5, sticky="e")
        self.entry_altezza = tk.Entry(self.frame_inputs, font=self.font_labels, width=20, borderwidth=1, relief="solid")
        self.entry_altezza.grid(row=2, column=1, padx=5, pady=5)

        # Pulsante per calcolare
        self.button_calcola = tk.Button(root, text=self.translations[self.current_language]["calculate"], font=self.font_button, bg="#28A745", fg="white", activebackground="#218838", activeforeground="white", command=self.calcola, relief="raised", borderwidth=1)
        self.button_calcola.grid(row=3, column=0, columnspan=2, pady=10)

        # Pulsante per mostrare le formule
        self.button_formule = tk.Button(root, text=self.translations[self.current_language]["formula_title"], font=self.font_button, bg="#007ACC", fg="white", activebackground="#0056A0", activeforeground="white", command=self.mostra_formule, relief="raised", borderwidth=1)
        self.button_formule.grid(row=4, column=0, columnspan=2, pady=10)

        # Etichetta per il risultato
        self.label_risultato = tk.Label(root, text="", font=self.font_result, bg="#F5F5F5", fg="#0056A0", wraplength=350)
        self.label_risultato.grid(row=5, column=0, columnspan=2, pady=10)

        # Menu a discesa per la selezione della lingua
        self.language_var = tk.StringVar(value=self.current_language)
        self.language_menu = ttk.Combobox(root, textvariable=self.language_var, values=["italiano", "english", "deutch", "Español", "中国人"], state="readonly")
        self.language_menu.grid(row=6, column=0, padx=10, pady=10, sticky="w")
        self.language_menu.bind("<<ComboboxSelected>>", self.cambia_lingua)

        # Crediti in fondo
        self.label_crediti = tk.Label(root, text="Sviluppato da Leo - 2024", font=self.font_error, bg="#F5F5F5", fg="#6C757D")
        self.label_crediti.grid(row=6, column=1, pady=10)

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
                self.show_error(self.translations[self.current_language]["error_base"])
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

            # Mostra il grafico del trapezio
            self.mostra_grafico(base_maggiore, base_minore, altezza)

        except ValueError:
            self.show_error(self.translations[self.current_language]["error_value"])

    def show_error(self, message):
        messagebox.showerror("Errore", message)
        self.label_risultato.config(text=message, fg="#FF4C4C")

    def calcola_area(self, base_maggiore, base_minore, altezza):
        return ((base_maggiore + base_minore) * altezza) / 2

    def calcola_perimetro(self, base_maggiore, base_minore, altezza):
        lato_obliquo = math.sqrt(((base_maggiore - base_minore) ** 2) / 4 + altezza ** 2)
        return base_maggiore + base_minore + 2 * lato_obliquo

    def mostra_grafico(self, base_maggiore, base_minore, altezza):
        # Calcolare la differenza tra le basi per centrare la base minore
        base_diff = (base_maggiore - base_minore) / 2

        # Coordinate dei vertici del trapezio simmetrico
        x = np.array([0, base_maggiore, base_maggiore - base_diff, base_diff, 0])
        y = np.array([0, 0, altezza, altezza, 0])

        # Creare il grafico
        plt.figure(figsize=(8, 6))
        plt.plot(x, y, 'b-', linewidth=2)
        plt.fill(x, y, 'lightblue', alpha=0.5)

        # Aggiungere etichette e griglia
        plt.title(self.translations[self.current_language]["graph_title"], fontsize=14, fontweight='bold')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.grid(True)
        plt.gca().set_aspect('equal', adjustable='box')

        # Mostrare il grafico
        plt.show()

    def mostra_formule(self):
        formula_text = self.translations[self.current_language]["formula_text"]
        messagebox.showinfo(self.translations[self.current_language]["formula_title"], formula_text)

    def cambia_lingua(self, event):
        self.current_language = self.language_var.get()

        # Aggiorna il testo dei widget
        self.label_title.config(text=self.translations[self.current_language]["title"])
        self.label_base_maggiore.config(text=self.translations[self.current_language]["base_maggiore"])
        self.label_base_minore.config(text=self.translations[self.current_language]["base_minore"])
        self.label_altezza.config(text=self.translations[self.current_language]["altezza"])
        self.button_calcola.config(text=self.translations[self.current_language]["calculate"])
        self.button_formule.config(text=self.translations[self.current_language]["formula_title"])
        self.label_risultato.config(text="", fg="#0056A0")
        plt.title(self.translations[self.current_language]["graph_title"], fontsize=14, fontweight='bold')

if __name__ == "__main__":
    root = tk.Tk()
    app = TrapezioIsosceleApp(root)
    root.mainloop()
