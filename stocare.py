import requests


#ZONA DANI
base_url = "https://the-trivia-api.com/v2/questions/"

def get_question(category,difficulty):
    url = f"{base_url}?categories={category}&difficulties={difficulty}"
    response = requests.get(url)
    return response.json()

get_question("science","easy")



#Zona lui Cosmmin