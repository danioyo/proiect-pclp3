import tkinter as tk
from stocare import get_question

def porneste_aplicatia():



    #ZONA DANI
    root = tk.Tk()
    root.title("Quiz App")
    root.geometry("800x500")


    #pagina 0(pagina de pornire)
    pagina_pornire = tk.Frame(root)
    pagina_pornire.pack()
    tk.Label(pagina_pornire, text="QUIZ", font=("Arial", 20)).pack(pady=20)
    grid_butoane_pornire = tk.Frame(pagina_pornire)
    grid_butoane_pornire.pack(pady=10)


    def go_to_pickName():
            pagina_pornire.pack_forget()
            pagina_nume.pack()

    
    tk.Button(grid_butoane_pornire, text="Start Quiz", width=15, height=2, command=go_to_pickName).grid(row=0, column=0, padx=10)
    tk.Button(grid_butoane_pornire, text="Ranking", width=15, height=2).grid(row=0, column=1, padx=10)





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

    def alege_categorie(categ):
        selectie["categorie"] = categ
        pagina_categorii.pack_forget()
        pagina_dificultate.pack()

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



    selectie = {"categorie":"", "dificultate": ""}
    

    def categorii(event):
        nume = entry_nume.get()
        pagina_nume.pack_forget()
        pagina_categorii.pack()

    entry_nume.bind("<Return>", categorii)









    #Zona lui Cosmmin






    #Zona lui Andrei












    root.mainloop() 