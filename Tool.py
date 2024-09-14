import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


class TrapezioIsosceleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calcolo Trapezio Isoscele")
        self.current_language = "italiano"
        self.current_theme = "light"

        # Definisci i temi
        self.theme_light = {
            "bg": "#F0F0F0",
            "fg": "#000000",
            "label_fg": "#333333",
            "button_bg": "#007BFF",
            "button_fg": "#FFFFFF",
            "formula_bg": "#FFFFFF",
            "result_fg": "#333333",
            "entry_bg": "#FFFFFF"
        }

        self.theme_dark = {
            "bg": "#2E2E2E",
            "fg": "#FFFFFF",
            "label_fg": "#DDDDDD",
            "button_bg": "#007BFF",
            "button_fg": "#FFFFFF",
            "formula_bg": "#3C3C3C",
            "result_fg": "#DDDDDD",
            "entry_bg": "#4A4A4A"
        }

        # Crea e applica il tema iniziale
        self.theme = self.theme_light if self.current_theme == "light" else self.theme_dark

        # Definisci le traduzioni
        self.translations = {
            "italiano": {
                "title": "Calcolo Trapezio Isoscele",
                "base_maggiore": "Base Maggiore:",
                "base_minore": "Base Minore:",
                "altezza": "Altezza:",
                "calculate": "Calcola",
                "formula_title": "Formule",
                "theme": "Tema",
                "error_message": "Inserisci valori numerici validi!",
                "error_title": "Errore",
                "formulas": "Area = ((Base Maggiore + Base Minore) / 2) * Altezza\nPerimetro = Base Maggiore + Base Minore + 2 * Lato Obliquo"
            },
            "inglese": {
                "title": "Isosceles Trapezoid Calculation",
                "base_maggiore": "Major Base:",
                "base_minore": "Minor Base:",
                "altezza": "Height:",
                "calculate": "Calculate",
                "formula_title": "Formulas",
                "theme": "Theme",
                "error_message": "Enter valid numeric values!",
                "error_title": "Error",
                "formulas": "Area = ((Major Base + Minor Base) / 2) * Height\nPerimeter = Major Base + Minor Base + 2 * Slant Side"
            },
            "spagnolo": {
                "title": "Cálculo Trapecio Isósceles",
                "base_maggiore": "Base Mayor:",
                "base_minore": "Base Menor:",
                "altezza": "Altura:",
                "calculate": "Calcular",
                "formula_title": "Fórmulas",
                "theme": "Tema",
                "error_message": "¡Ingresa valores numéricos válidos!",
                "error_title": "Error",
                "formulas": "Área = ((Base Mayor + Base Menor) / 2) * Altura\nPerímetro = Base Mayor + Base Menor + 2 * Lado Oblicuo"
            },
            "cinese": {
                "title": "等腰梯形计算",
                "base_maggiore": "大底边:",
                "base_minore": "小底边:",
                "altezza": "高度:",
                "calculate": "计算",
                "formula_title": "公式",
                "theme": "主题",
                "error_message": "请输入有效的数字值！",
                "error_title": "错误",
                "formulas": "面积 = ((大底边 + 小底边) / 2) * 高度\n周长 = 大底边 + 小底边 + 2 * 斜边"
            },
        }

        # Definisci i loghi ASCII
        self.logos = {
            "italiano": (
                "████████╗██████╗  █████╗ ██████╗ ███████╗███████╗██╗ ██████╗ \n"
                "╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══███╔╝██║██╔═══██╗\n"
                "   ██║   ██████╔╝███████║██████╔╝█████╗    ███╔╝ ██║██║   ██║\n"
                "   ██║   ██╔══██╗██╔══██║██╔═══╝ ██╔══╝   ███╔╝  ██║██║   ██║\n"
                "   ██║   ██║  ██║██║  ██║██║     ███████╗███████╗██║╚██████╔╝\n"
                "   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚══════╝╚═╝ ╚═════╝ \n"
            ),
            "inglese": (
                "████████╗██████╗  █████╗ ██████╗ ███████╗███████╗██╗ ██╗   ██╗███╗   ███╗\n"
                "╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══███╔╝██║ ██║   ██║████╗ ████║\n"
                "   ██║   ██████╔╝███████║██████╔╝█████╗    ███╔╝ ██║ ██║   ██║██╔████╔██║\n"
                "   ██║   ██╔══██╗██╔══██║██╔═══╝ ██╔══╝   ███╔╝  ██║ ██║   ██║██║╚██╔╝██║\n"
                "   ██║   ██║  ██║██║  ██║██║     ███████╗███████╗██║ ╚██████╔╝██║ ╚═╝ ██║\n"
                "   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚══════╝     ╚═════╝ ╚═╝     ╚═╝\n"
            ),
            "spagnolo": (
                "████████╗██████╗  █████╗ ██████╗ ███████╗███████╗██████╗ ██╗██████╗ ███████╗\n"
                "╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔════╝╚══███╔╝██╔═══██╗██║██╔══██╗██╔════╝\n"
                "   ██║   ██████╔╝███████║██████╔╝█████╗   ███╔╝  ██║   ██║██║██║  ██║█████╗  \n"
                "   ██║   ██╔══██╗██╔══██║██╔═══╝ ██╔══╝   ███╔╝  ██║   ██║██║██║  ██║██╔══╝  \n"
                "   ██║   ██║  ██║██║  ██║██║     ███████╗███████╗╚██████╔╝██║██████╔╝███████╗\n"
                "   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚══════╝╚══════╝ ╚═════╝ ╚═╝╚═════╝ ╚══════╝\n"
            ),
            "cinese": (
                "梯形\n"
            ),
        }

        # Creazione degli attributi dell'interfaccia utente
        self.create_widgets()
        self.apply_theme(self.current_theme)
        self.update_texts()

    def create_widgets(self):
        # Logo e titolo
        self.label_logo = tk.Label(self.root, text=self.get_logo(), font=("Courier", 10), bg=self.theme["bg"],
                                   fg=self.theme["fg"], anchor="center", justify="center")
        self.label_logo.grid(row=0, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

        self.label_title = tk.Label(self.root, text=self.translations[self.current_language]["title"],
                                    font=("Arial", 14), bg=self.theme["bg"], fg=self.theme["fg"], anchor="center")
        self.label_title.grid(row=1, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

        # Frame per i campi di input
        self.frame_inputs = tk.Frame(self.root, bg=self.theme["formula_bg"])
        self.frame_inputs.grid(row=2, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

        self.label_base_maggiore = tk.Label(self.frame_inputs,
                                            text=self.translations[self.current_language]["base_maggiore"],
                                            bg=self.theme["formula_bg"], fg=self.theme["label_fg"])
        self.label_base_maggiore.grid(row=0, column=0, pady=5, sticky="e")

        self.entry_base_maggiore = tk.Entry(self.frame_inputs, bg=self.theme["entry_bg"])
        self.entry_base_maggiore.grid(row=0, column=1, pady=5, sticky="w")

        self.label_base_minore = tk.Label(self.frame_inputs,
                                          text=self.translations[self.current_language]["base_minore"],
                                          bg=self.theme["formula_bg"], fg=self.theme["label_fg"])
        self.label_base_minore.grid(row=1, column=0, pady=5, sticky="e")

        self.entry_base_minore = tk.Entry(self.frame_inputs, bg=self.theme["entry_bg"])
        self.entry_base_minore.grid(row=1, column=1, pady=5, sticky="w")

        self.label_altezza = tk.Label(self.frame_inputs, text=self.translations[self.current_language]["altezza"],
                                      bg=self.theme["formula_bg"], fg=self.theme["label_fg"])
        self.label_altezza.grid(row=2, column=0, pady=5, sticky="e")

        self.entry_altezza = tk.Entry(self.frame_inputs, bg=self.theme["entry_bg"])
        self.entry_altezza.grid(row=2, column=1, pady=5, sticky="w")

        # Bottone Calcola
        self.button_calcola = tk.Button(self.root, text=self.translations[self.current_language]["calculate"],
                                        command=self.calcola, bg=self.theme["button_bg"], fg=self.theme["button_fg"])
        self.button_calcola.grid(row=3, column=0, pady=10, padx=10, sticky="ew")

        # Bottone Formule
        self.button_formule = tk.Button(self.root, text=self.translations[self.current_language]["formula_title"],
                                        command=self.mostra_formule, bg="#FFC300", fg="black")
        self.button_formule.grid(row=3, column=1, pady=10, padx=10, sticky="ew")

        # Etichetta Risultato
        self.label_risultato = tk.Label(self.root, text="", bg=self.theme["bg"], fg=self.theme["result_fg"])
        self.label_risultato.grid(row=4, column=0, columnspan=2, pady=10, padx=10, sticky="ew")

        # Bottone Tema
        self.button_theme = tk.Button(self.root, text=self.translations[self.current_language]["theme"],
                                      command=self.toggle_theme, bg="#FF5733", fg="#FFFFFF")
        self.button_theme.grid(row=5, column=0, pady=10, padx=10, sticky="ew")

        # Menu Lingua
        self.language_menu = ttk.Combobox(self.root, values=["italiano", "inglese", "spagnolo", "cinese"],
                                          state="readonly")
        self.language_menu.set(self.current_language)
        self.language_menu.grid(row=5, column=1, pady=10, padx=10, sticky="ew")
        self.language_menu.bind("<<ComboboxSelected>>", self.change_language)

    def get_logo(self):
        return self.logos.get(self.current_language, self.logos["italiano"])

    def apply_theme(self, theme):
        if theme == "light":
            self.theme = self.theme_light
        else:
            self.theme = self.theme_dark

        # Applica il tema a tutti i widget
        self.root.configure(bg=self.theme["bg"])
        self.label_logo.configure(bg=self.theme["bg"], fg=self.theme["fg"])
        self.label_title.configure(bg=self.theme["bg"], fg=self.theme["fg"])
        self.frame_inputs.configure(bg=self.theme["formula_bg"])
        self.label_base_maggiore.configure(bg=self.theme["formula_bg"], fg=self.theme["label_fg"])
        self.label_base_minore.configure(bg=self.theme["formula_bg"], fg=self.theme["label_fg"])
        self.label_altezza.configure(bg=self.theme["formula_bg"], fg=self.theme["label_fg"])
        self.button_calcola.configure(bg=self.theme["button_bg"], fg=self.theme["button_fg"])
        self.button_formule.configure(bg="#FFC300", fg="black")
        self.label_risultato.configure(bg=self.theme["bg"], fg=self.theme["result_fg"])
        self.button_theme.configure(bg="#FF5733", fg="#FFFFFF")
        self.language_menu.configure(style="TCombobox")

    def toggle_theme(self):
        self.current_theme = "dark" if self.current_theme == "light" else "light"
        self.apply_theme(self.current_theme)

    def update_texts(self):
        self.label_title.config(text=self.translations[self.current_language]["title"])
        self.label_base_maggiore.config(text=self.translations[self.current_language]["base_maggiore"])
        self.label_base_minore.config(text=self.translations[self.current_language]["base_minore"])
        self.label_altezza.config(text=self.translations[self.current_language]["altezza"])
        self.button_calcola.config(text=self.translations[self.current_language]["calculate"])
        self.button_formule.config(text=self.translations[self.current_language]["formula_title"])
        self.button_theme.config(text=self.translations[self.current_language]["theme"])
        self.language_menu.set(self.current_language)
        self.label_risultato.config(text="", fg=self.theme["result_fg"])
        self.label_logo.config(text=self.get_logo())  # Aggiorna il logo

    def calcola(self):
        try:
            base_maggiore = float(self.entry_base_maggiore.get())
            base_minore = float(self.entry_base_minore.get())
            altezza = float(self.entry_altezza.get())

            # Calcolo area e perimetro
            area = ((base_maggiore + base_minore) / 2) * altezza
            perimetro = base_maggiore + base_minore + 2 * np.sqrt((altezza**2 + ((base_maggiore - base_minore) / 2)**2))

            self.label_risultato.config(text=f"Area: {area:.2f}\nPerimetro: {perimetro:.2f}")

            # Mostra il grafico in una finestra separata
            self.mostra_grafico(base_maggiore, base_minore, altezza)
        except ValueError:
            messagebox.showerror(self.translations[self.current_language]["error_title"],
                                 self.translations[self.current_language]["error_message"])

    def mostra_formule(self):
        messagebox.showinfo(self.translations[self.current_language]["formula_title"],
                            self.translations[self.current_language]["formulas"])

    def mostra_grafico(self, base_maggiore, base_minore, altezza):
        # Crea una nuova finestra per il grafico
        grafico_finestra = tk.Toplevel(self.root)
        grafico_finestra.title("Grafico Trapezio Isoscele")

        fig, ax = plt.subplots()
        ax.set_title('Trapezio Isoscele')
        ax.set_xlabel('Base')
        ax.set_ylabel('Altezza')

        # Dati del trapezio
        # Calcola la lunghezza dei lati obliqui
        lato_obliquo = np.sqrt((altezza**2) + ((base_maggiore - base_minore) / 2)**2)

        # Coordinate dei vertici
        x = [0, base_maggiore, base_maggiore - (base_maggiore - base_minore) / 2, (base_maggiore - base_minore) / 2, 0]
        y = [0, 0, altezza, altezza, 0]

        ax.plot(x, y, marker='o')
        ax.fill(x, y, 'b', alpha=0.1)  # Aggiunge un riempimento leggero per la chiarezza

        # Mostra il grafico nella finestra separata
        canvas = FigureCanvasTkAgg(fig, master=grafico_finestra)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

    def change_language(self, event):
        self.current_language = self.language_menu.get()
        self.update_texts()
        self.apply_theme(self.current_theme)


if __name__ == "__main__":
    root = tk.Tk()
    app = TrapezioIsosceleApp(root)
    root.mainloop()
