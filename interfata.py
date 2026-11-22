import tkinter as tk
from tkinter import ttk, messagebox
from stocare import incarca_clasament, get_question, salveaza_scor
from logica import pregateste_intrebari, SesiuneQuiz

def init_clasament_cosmin(root, pagina_pornire, pagina_nume, pagina_categorii, pagina_intrebari):
    pagina_clasament = tk.Frame(root)
    tk.Label(pagina_clasament, text="Clasament", font=("Arial", 20)).pack(pady=15)

    coloane = ("loc", "nume", "scor", "categorie")
    tabel_clasament = ttk.Treeview(pagina_clasament, columns=coloane, show="headings", height=10)
    for col, titlu in [("loc", "#"), ("nume", "Nume"), ("scor", "Scor"), ("categorie", "Categorie")]:
        tabel_clasament.heading(col, text=titlu)
        tabel_clasament.column(col, width=140 if col != "loc" else 50, anchor="center")
    tabel_clasament.pack(pady=10)

    def incarca_tabel():
        for rand in tabel_clasament.get_children():
            tabel_clasament.delete(rand)
        for idx, item in enumerate(incarca_clasament(), start=1):
            tabel_clasament.insert(
                "",
                "end",
                values=(idx, item.get("nume", ""), item.get("scor", 0), item.get("categorie", "")),
            )

    def inchide_clasament():
        pagina_clasament.pack_forget()
        pagina_pornire.pack()

    def deschide_clasament():
        pagina_pornire.pack_forget()
        pagina_nume.pack_forget()
        pagina_categorii.pack_forget()
        pagina_intrebari.pack_forget()
        incarca_tabel()
        pagina_clasament.pack(fill="both", expand=True)

    tk.Button(pagina_clasament, text="Înapoi", width=15, command=inchide_clasament).pack(pady=10)
    return deschide_clasament


def porneste_aplicatia():

    #ZONA DANI
    root = tk.Tk()
    root.title("Quiz App")
    root.geometry("800x500")

    selectie = {"nume": "", "categorie": "", "dificultate": ""}

    #functii
    def go_to_pickName():
            pagina_pornire.pack_forget()
            pagina_nume.pack()

    def alege_categorie(categ):
            selectie["categorie"] = categ
            pagina_categorii.pack_forget()
            pagina_dificultate.pack()

    def categorii(event=None):
        selectie["nume"] = entry_nume.get().strip() or "Anonim"
        pagina_nume.pack_forget()
        pagina_categorii.pack()



    #pagina 0(pagina de pornire)
    pagina_pornire = tk.Frame(root)
    pagina_pornire.pack()
    tk.Label(pagina_pornire, text="QUIZ", font=("Arial", 20)).pack(pady=20)
    grid_butoane_pornire = tk.Frame(pagina_pornire)
    grid_butoane_pornire.pack(pady=10)

    tk.Button(grid_butoane_pornire, text="Start Quiz", width=15, height=2, command=go_to_pickName).grid(row=0, column=0, padx=10)
    btn_ranking = tk.Button(grid_butoane_pornire, text="Ranking", width=15, height=2)
    btn_ranking.grid(row=0, column=1, padx=10)

    #pag 1(nume)
    pagina_nume = tk.Frame(root)
    tk.Label(pagina_nume, text="PICK NAME", font=("Arial", 20)).pack(pady=20)

    entry_nume = tk.Entry(pagina_nume, width=25)
    entry_nume.pack(pady=10)

    #pag 2(categoriile)
    pagina_categorii = tk.Frame(root)
    tk.Label(pagina_categorii, text="Categories:", font=("Arial", 20)).pack(pady=20)

    grid_butoane = tk.Frame(pagina_categorii)
    grid_butoane.pack(pady=10)

    tk.Button(grid_butoane, text="Science", width=15, height=3, command=lambda: alege_categorie("science")).grid(row=0, column=0, padx=10, pady=10)
    tk.Button(grid_butoane, text="History", width=15, height=3, command=lambda: alege_categorie("history")).grid(row=0, column=1, padx=10, pady=10)
    tk.Button(grid_butoane, text="Music", width=15, height=3, command=lambda: alege_categorie("music")).grid(row=1, column=0, padx=10, pady=10)
    tk.Button(grid_butoane, text="Geography", width=15, height=3, command=lambda: alege_categorie("geography")).grid(row=1, column=1, padx=10, pady=10)

    #pag 3(dificultate)
    pagina_dificultate = tk.Frame(root)
    tk.Label(pagina_dificultate,text="Choose Difficulty:", font=("Arial", 20)).pack(pady=20)

    tk.Button(pagina_dificultate, text="Easy", width=15, height=2, command=lambda: alege_dificultate("easy")).pack(pady=5)
    tk.Button(pagina_dificultate, text="Medium", width=15, height=2, command=lambda: alege_dificultate("medium")).pack(pady=5)
    tk.Button(pagina_dificultate, text="Hard", width=15, height=2, command=lambda: alege_dificultate("hard")).pack(pady=5)

    #pag 4(intrebari)
    pagina_intrebari = tk.Frame(root)
    tk.Label(pagina_intrebari, text="Intrebari:", font=("Arial", 20)).pack(pady=20)

    entry_nume.bind("<Return>", categorii)

    #Zona lui Cosmmin
    deschide = init_clasament_cosmin(root, pagina_pornire, pagina_nume, pagina_categorii, pagina_intrebari)
    btn_ranking.config(command=deschide)

    #Zona lui Andrei
    sesiune_curenta = {"quiz": None}

    def inapoi_la_meniu():
        pagina_intrebari.pack_forget()
        pagina_pornire.pack()

    def afiseaza_ecran_final():
        for widget in pagina_intrebari.winfo_children():
            widget.destroy()

        quiz = sesiune_curenta["quiz"]
        total = len(quiz.intrebari)

        salveaza_scor(selectie["nume"], quiz.scor, selectie["categorie"])

        tk.Label(pagina_intrebari, text="Quiz Finalizat!", font=("Arial", 22, "bold")).pack(pady=25)
        tk.Label(pagina_intrebari, text=f"Jucător: {selectie['nume']}", font=("Arial", 14)).pack(pady=5)
        tk.Label(
            pagina_intrebari,
            text=f"Scor obținut: {quiz.scor} / {total}",
            font=("Arial", 18, "bold"),
            fg="dark green",
        ).pack(pady=15)

        frame_butoane_final = tk.Frame(pagina_intrebari)
        frame_butoane_final.pack(pady=20)

        tk.Button(frame_butoane_final, text="Vezi Clasamentul", width=18, height=2, command=deschide).grid(row=0, column=0, padx=10)
        tk.Button(frame_butoane_final, text="Meniu Principal", width=18, height=2, command=inapoi_la_meniu).grid(row=0, column=1, padx=10)

    def randeaza_intrebare():
        for widget in pagina_intrebari.winfo_children():
            widget.destroy()

        quiz = sesiune_curenta["quiz"]
        if quiz.este_terminat():
            afiseaza_ecran_final()
            return

        date_intrebare = quiz.intrebare_curenta()
        nr_curent = quiz.index_curent + 1
        total = len(quiz.intrebari)

        tk.Label(
            pagina_intrebari,
            text=f"Întrebarea {nr_curent} / {total}   |   Scor: {quiz.scor}",
            font=("Arial", 12, "bold"),
            fg="gray35",
        ).pack(pady=(20, 10))

        tk.Label(
            pagina_intrebari,
            text=date_intrebare["intrebare"],
            font=("Arial", 15, "bold"),
            wraplength=680,
            justify="center",
        ).pack(pady=20, padx=20)

        butoane_optiuni = []

        def on_raspuns(idx_ales):
            for btn in butoane_optiuni:
                btn.config(state="disabled")

            este_corect, idx_corect = quiz.verifica_raspuns(idx_ales)

            butoane_optiuni[idx_corect].config(bg="green", fg="white", disabledforeground="white")
            if not este_corect:
                butoane_optiuni[idx_ales].config(bg="red", fg="white", disabledforeground="white")

            # Pauza scurta pentru a vedea raspunsul corect
            root.after(800, randeaza_intrebare)

        for idx, text_optiune in enumerate(date_intrebare["optiuni"]):
            btn = tk.Button(
                pagina_intrebari,
                text=text_optiune,
                font=("Arial", 12),
                width=45,
                pady=8,
                command=lambda i=idx: on_raspuns(i),
            )
            btn.pack(pady=6)
            butoane_optiuni.append(btn)

    def alege_dificultate(dif):
        selectie["dificultate"] = dif
        try:
            date_brute = get_question(selectie["categorie"], dif)
            intrebari = pregateste_intrebari(date_brute, numar_intrebari=5)
        except Exception as e:
            messagebox.showerror("Eroare", f"Nu s-au putut încărca întrebările:\n{e}")
            return

        if not intrebari:
            messagebox.showwarning("Atenție", "Nu s-au găsit întrebări pentru această selecție.")
            return

        sesiune_curenta["quiz"] = SesiuneQuiz(intrebari)
        pagina_dificultate.pack_forget()
        pagina_intrebari.pack(fill="both", expand=True)
        randeaza_intrebare()


    root.mainloop()