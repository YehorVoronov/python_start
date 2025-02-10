
import requests

base_url = "https://pokeapi.co/api/v2/pokemon/"

def get_pokemon(name):
    response = requests.get(url=f"{base_url}{name}")
    # print(f"{base_url}{name}")
    # print(response.status_code)
    # print(response.json())
    return response.json()

# pokemon_name = "pikachu"
pokemon_name = "typhlosion"

pokemon_info = get_pokemon(pokemon_name)

print(pokemon_info["name"].capitalize())
print(pokemon_info["id"])
print(pokemon_info["height"])
print(pokemon_info["weight"])