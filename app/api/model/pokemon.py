import requests
import random
import json

class PokemonModel:
    def __init__(self, pokemon):
        pokeapi_api_url = 'https://pokeapi.co/api/v2/pokemon-species/'+pokemon
        response = requests.get(url=pokeapi_api_url)
        data = response.json()
        descriptions = data["flavor_text_entries"]
        english_description = []
        for description in descriptions:
            if description['language']['name'] == "en":
                english_description.append(description['flavor_text'])

        lucky_one = random.choice(english_description)

        shakespeare_api_url = "https://api.funtranslations.com/translate/shakespeare.json"
        response = requests.post(url=shakespeare_api_url, data={'text': lucky_one})
        data = response.json()
        self.name = pokemon
        self.description = data['contents']['translated']

        


