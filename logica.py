def creeaza_intrebare(intrebare, optiuni, index):
    intrebare = intrebare.strip()
    if(intrebare == ""):
        raise ValueError("intrebarea nu exista!!")
    if(len(optiuni)<2):
        raise ValueError("2 optiuni minim!!")
    if(0<=index<len(optiuni)):
        raise ValueError("index invalid")
    return {
        "intrebare": intrebare,
        "optiuni": optiuni,
        "raspuns_corect": index
    }