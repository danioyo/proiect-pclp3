import random


def pregateste_intrebari(date_brute, numar_intrebari=5):
    if not date_brute:
        return []

    intrebari_procesate = []

    for item in date_brute:
        # Formatul primit de la API (stocare.py)
        if "correctAnswer" in item and "incorrectAnswers" in item:
            if isinstance(item.get("question"), dict):
                text_intrebare = item["question"].get("text", "")
            else:
                text_intrebare = str(item.get("question", ""))

            raspuns_corect = item["correctAnswer"]
            optiuni = list(item["incorrectAnswers"]) + [raspuns_corect]
            random.shuffle(optiuni)
            index_corect = optiuni.index(raspuns_corect)

            intrebari_procesate.append({
                "intrebare": text_intrebare,
                "optiuni": optiuni,
                "raspuns_corect": index_corect,
            })

        # Formatul din fisierul JSON local
        elif "intrebare" in item and "optiuni" in item and "raspuns_corect" in item:
            optiuni = list(item["optiuni"])
            raspuns_corect = optiuni[item["raspuns_corect"]]
            random.shuffle(optiuni)
            index_corect = optiuni.index(raspuns_corect)

            intrebari_procesate.append({
                "intrebare": item["intrebare"],
                "optiuni": optiuni,
                "raspuns_corect": index_corect,
            })

    if len(intrebari_procesate) <= numar_intrebari:
        random.shuffle(intrebari_procesate)
        return intrebari_procesate

    return random.sample(intrebari_procesate, numar_intrebari)


class SesiuneQuiz:
    def __init__(self, intrebari):
        self.intrebari = intrebari
        self.index_curent = 0
        self.scor = 0

    def intrebare_curenta(self):
        if self.este_terminat():
            return None
        return self.intrebari[self.index_curent]

    def este_terminat(self):
        return self.index_curent >= len(self.intrebari)

    def verifica_raspuns(self, index_ales):
        intrebare = self.intrebare_curenta()
        if intrebare is None:
            return False, -1

        index_corect = intrebare["raspuns_corect"]
        este_corect = (index_ales == index_corect)

        if este_corect:
            self.scor += 1

        self.index_curent += 1
        return este_corect, index_corect