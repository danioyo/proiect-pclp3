import tkinter as tk

def porneste_aplicatia():



    #ZONA DANI
    root = tk.Tk()
    root.title("Quiz App")
    root.geometry("800x500")

    #pag 1(nume)
    pagina_nume = tk.Frame(root)
    pagina_nume.pack()
    label_intrebare = tk.Label(pagina_nume, text="PICK NAME", font=("Arial", 20))
    label_intrebare.pack(pady=20)
    
    entry_nume = tk.Entry(pagina_nume, width=25)
    entry_nume.pack(pady=10)

    #pag 2(categoriile)
    pagina_categorii = tk.Frame(root)
    tk.Label(pagina_categorii, text="Categories:", font=("Arial", 20)).pack(pady=20)

    grid_butoane = tk.Frame(pagina_categorii)
    grid_butoane.pack(pady=10)

    tk.Button(grid_butoane, text="Science", width=15, height=3).grid(row=0, column=0, padx=10, pady=10)
    tk.Button(grid_butoane, text="History", width=15, height=3).grid(row=0, column=1, padx=10, pady=10)
    tk.Button(grid_butoane, text="Music", width=15, height=3).grid(row=1, column=0, padx=10, pady=10)
    tk.Button(grid_butoane, text="Geography", width=15, height=3).grid(row=1, column=1, padx=10, pady=10)


    #pag 3(intrebari)
    pagina_intrebari = tk.Frame(root)
    tk.Label(pagina_intrebari, text="Intrebari:", font=("Arial", 20)).pack(pady=20)


    def alegere_categ(categ):
        pagina_categorii.pack_forget()
        pagina_intrebari.pack()

    tk.Button(grid_butoane, )

    def categorii(event):
        nume = entry_nume.get()
        pagina_nume.pack_forget()
        pagina_categorii.pack()

    entry_nume.bind("<Return>", categorii)

    root.mainloop() 









    #Zona lui Cosmmin

from tkinter import ttk
from stocare import incarca_clasament


def init_clasament_cosmin(root, pagina_nume, pagina_categorii, pagina_intrebari):
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
        pagina_categorii.pack()

    def deschide_clasament():
        pagina_nume.pack_forget()
        pagina_categorii.pack_forget()
        pagina_intrebari.pack_forget()
        incarca_tabel()
        pagina_clasament.pack(fill="both", expand=True)

    tk.Button(pagina_clasament, text="Înapoi", width=15, command=inchide_clasament).pack(pady=10)
    tk.Button(pagina_categorii, text="Clasament", width=15, command=deschide_clasament).pack(pady=10)




    #Zona lui Andrei
