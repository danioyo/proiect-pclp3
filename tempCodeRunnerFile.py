import tkinter as tk
from tkinter import messagebox

# --- PALETA DE CULORI (preluată din style.css) ---
BG_COLOR = "#0F172A"       # var(--blue)
BTN_COLOR = "#b44343"      # var(--red)
TEXT_COLOR = "#F8F9FA"     # var(--white)
CARD_BG = "#1f2f53"        # fundalul panoului central

# --- STRUCTURA DE DATE (liste și dicționare cerute la PCLP) ---
intrebari_pe_categorii = {
    "General Knowledge": [
        {
            "id": 1,
            "intrebare": "Care este capitala Frantei?",
            "optiuni": ["Berlin", "Madrid", "Paris", "Roma"],
            "corect": "Paris"
        },
        {
            "id": 2,
            "intrebare": "Cate continente exista pe Pamant?",
            "optiuni": ["5", "6", "7", "8"],
            "corect": "7"
        }
    ],
    "Science": [
        {
            "id": 1,
            "intrebare": "Care este formula chimica a apei?",
            "optiuni": ["CO2", "H2O", "O2", "NaCl"],
            "corect": "H2O"
        }
    ]
}

categorii_disponibile = [
    "Music", "Sport & Leisure", "Film & TV", "Science",
    "History", "Geography", "Art & Literature", "Food & Drinks",
    "General Knowledge", "Society & Culture", "Random"
]

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("850x650")
        self.root.configure(bg=BG_COLOR)

        self.scor = 0
        self.intrebari_curente = []
        self.index_intrebare = 0

        # Creare containere (Ecrane)
        self.frame_start = tk.Frame(self.root, bg=BG_COLOR)
        self.frame_categorii = tk.Frame(self.root, bg=BG_COLOR)
        self.frame_intrebare = tk.Frame(self.root, bg=BG_COLOR)

        self.construieste_ecran_start()
        self.construieste_ecran_categorii()
        self.construieste_ecran_intrebare()

        # Afiseaza ecranul initial de start
        self.frame_start.pack(expand=True)

    # 1. ECRAN DE START (corespunde butonului din script.js)
    def construieste_ecran_start(self):
        lbl_logo = tk.Label(
            self.frame_start, text="QUIZ", 
            font=("Montserrat", 48, "bold"), fg=TEXT_COLOR, bg=BG_COLOR
        )
        lbl_logo.pack(pady=30)

        btn_start = tk.Button(
            self.frame_start, text="Start Quiz", 
            font=("Inter", 20, "bold"), bg=BTN_COLOR, fg=TEXT_COLOR,
            padx=20, pady=10, relief="flat", cursor="hand2",
            command=self.arata_categorii
        )
        btn_start.pack()

    # 2. ECRAN SELECTIE CATEGORII (corespunde grilei din main_page.html)
    def construieste_ecran_categorii(self):
        lbl_titlu = tk.Label(
            self.frame_categorii, text="Categorii", 
            font=("Poppins", 26, "bold"), fg=TEXT_COLOR, bg=BG_COLOR
        )
        lbl_titlu.pack(pady=15)

        container_grid = tk.Frame(self.frame_categorii, bg=CARD_BG, padx=20, pady=20)
        container_grid.pack(padx=20, pady=10)

        # Generare butoane pe 3 coloane (grid layout)
        for i, nume_cat in enumerate(categorii_disponibile):
            rand = i // 3
            coloana = i % 3
            btn = tk.Button(
                container_grid, text=nume_cat, 
                font=("Inter", 11, "bold"), bg=BTN_COLOR, fg=TEXT_COLOR,
                width=16, height=3, relief="flat", cursor="hand2",
                command=lambda c=nume_cat: self.porneste_quiz(c)
            )
            btn.grid(row=rand, column=coloana, padx=8, pady=8)

    # 3. ECRAN INTREBARE SI RASPUNSURI
    def construieste_ecran_intrebare(self):
        self.lbl_cat = tk.Label(
            self.frame_intrebare, text="", 
            font=("Poppins", 14), fg=TEXT_COLOR, bg=BG_COLOR
        )
        self.lbl_cat.pack(pady=5)

        self.lbl_intrebare = tk.Label(
            self.frame_intrebare, text="", wraplength=700,
            font=("Inter", 18, "bold"), fg=TEXT_COLOR, bg=BG_COLOR
        )
        self.lbl_intrebare.pack(pady=25)

        self.butoane_optiuni = []
        for _ in range(4):
            btn = tk.Button(
                self.frame_intrebare, text="", 
                font=("Inter", 13), bg=CARD_BG, fg=TEXT_COLOR,
                width=45, pady=8, relief="flat", cursor="hand2"
            )
            btn.pack(pady=6)
            self.butoane_optiuni.append(btn)

    # --- LOGICA DE TRANZITIE SI VERIFICARE ---
    def ascunde_toate_ecranele(self):
        self.frame_start.pack_forget()
        self.frame_categorii.pack_forget()
        self.frame_intrebare.pack_forget()

    def arata_categorii(self):
        self.ascunde_toate_ecranele()
        self.frame_categorii.pack(expand=True)

    def porneste_quiz(self, categorie):
        if categorie not in intrebari_pe_categorii or not intrebari_pe_categorii[categorie]:
            messagebox.showinfo("Info", f"Nu exista inca intrebari pentru categoria '{categorie}'.")
            return

        self.intrebari_curente = intrebari_pe_categorii[categorie]
        self.index_intrebare = 0
        self.scor = 0
        self.lbl_cat.config(text=f"Categorie: {categorie}")

        self.ascunde_toate_ecranele()
        self.frame_intrebare.pack(expand=True)
        self.incarca_intrebarea()

    def incarca_intrebarea(self):
        date_intrebare = self.intrebari_curente[self.index_intrebare]
        self.lbl_intrebare.config(text=f"{self.index_intrebare + 1}. {date_intrebare['intrebare']}")

        for i, optiune in enumerate(date_intrebare["optiuni"]):
            btn = self.butoane_optiuni[i]
            btn.config(
                text=optiune,
                command=lambda opt=optiune: self.verifica_raspuns(opt, date_intrebare["corect"])
            )

    def verifica_raspuns(self, ales, corect):
        if ales == corect:
            self.scor += 1
            messagebox.showinfo("Rezultat", "Corect!")
        else:
            messagebox.showwarning("Rezultat", f"Gresit! Raspunsul corect era: {corect}")

        self.index_intrebare += 1
        if self.index_intrebare < len(self.intrebari_curente):
            self.incarca_intrebarea()
        else:
            messagebox.showinfo(
                "Final", 
                f"Ai terminat quiz-ul!\nScor: {self.scor}/{len(self.intrebari_curente)}"
            )
            self.arata_categorii()

# Rulare aplicatie
if __name__ == "__main__":
    radacina = tk.Tk()
    app = QuizApp(radacina)
    radacina.mainloop()