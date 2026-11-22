import requests


#ZONA DANI
base_url = "https://the-trivia-api.com/v2/questions/"

def get_question(category,difficulty):
    url = f"{base_url}?categories={category}&difficulties={difficulty}"
    response = requests.get(url)
    return response.json()

get_question("science","easy")



#Zona lui Cosmmin

import json
import os

CLASAMENT_FILE = "clasament.json"


def sorteaza_clasament(intrari):
    return sorted(
        intrari,
        key=lambda item: (-int(item.get("scor", 0)), str(item.get("nume", "")).lower()),
    )


def incarca_clasament(fisier=CLASAMENT_FILE):
    if not os.path.exists(fisier):
        return []

    try:
        with open(fisier, "r", encoding="utf-8") as f:
            date = json.load(f)
        if not isinstance(date, list):
            return []
    except (json.JSONDecodeError, OSError):
        return []

    return sorteaza_clasament(date)


def salveaza_scor(nume, scor, categorie="General", fisier=CLASAMENT_FILE):
    nume_curat = (nume or "Anonim").strip() or "Anonim"
    categorie_curata = (categorie or "General").strip() or "General"

    try:
        scor_int = int(scor)
    except (TypeError, ValueError):
        scor_int = 0

    clasament = incarca_clasament(fisier)
    clasament.append({
        "nume": nume_curat,
        "scor": scor_int,
        "categorie": categorie_curata,
    })

    clasament_sortat = sorteaza_clasament(clasament)

    with open(fisier, "w", encoding="utf-8") as f:
        json.dump(clasament_sortat, f, indent=4, ensure_ascii=False)

    return clasament_sortat
