import tkinter as tk

def porneste_aplicatia():
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




    def categorii(event):
        nume = entry_nume.get()
        pagina_nume.pack_forget()
        pagina_categorii.pack()

    entry_nume.bind("<Return>", categorii)

    root.mainloop() 