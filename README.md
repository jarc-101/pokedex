# pokedex

It uses the pokemon API to get the details of pokemon input then returns the **Name**
 , **ID**, and **Base XP**. 

## Code
```python
import requests
import sys


def search_pokemon(name):
  response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}/")
  pokemon = response.json()
  print_pokemon(pokemon)

def print_pokemon(pokemon):
  print(f"Name: {pokemon['name'].capitalize()}")
  print(f"ID: {pokemon['id']}")
  print(f"Base XP: {pokemon['base_experience']}")


if __name__ == "__main__":
  search_pokemon(sys.argv[1])
```

See full code: [pokedex.py](https://github.com/jarc-101/pokedex/blob/main/pokedex.py)

# six_pokemon
Is my solution to a challenge given by our AWS intructor.

## Challenge
Create a pokemon team of 6 and output their Name:,HP:,Held Item:,Moveset:.

## Code/Solution
```python
import requests
import random

def search_pokemon(name):
  response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}/")
  pokemon = response.json()
  add_pokemon(pokemon)

def add_pokemon(pokemon):
  Name = f"Name: {pokemon['name'].capitalize()}"
  hp = f"HP: {pokemon['stats'][0]['base_stat']}"
  print(Name)
  print(hp)
  add_items(pokemon)

def add_items(pokemon):
  items = f"Held Items: {pokemon['held_items']}"
  if len(pokemon['held_items']) == 0:
    items_print = "Held Item: No item held"
  else:
    items = [item['item']['name'] for item in pokemon['held_items']]
    items = random.sample(items,1)
    items_print = f"Held Item: {items[0]}"
  print(items_print)
  get_moves(pokemon)

def get_moves(pokemon):
  moves = [move['move']['name'] for move in pokemon['moves']]
  moveset = random.sample(moves,4)
  print(f"Moveset: {moveset[0]}, {moveset[1]}, {moveset[2]}, {moveset[3]}\n")


if __name__ == "__main__":
  poke_num = 0
  team = [] # list for the team generation
  while poke_num != 6:
    poke_name = input("Choose your Pokemon: ").lower()
    try:
      search_pokemon(poke_name)
      team.append(poke_name)
      poke_num +=1
    except:
      print("Pokemon doesn't exist")

print("Gotta catch em' all")
print(team)
```

See full code with comments : [pokedex.py](https://github.com/jarc-101/pokedex/blob/main/six_pokemon.py)


### I also created an app using streamlit to explore python more
Here's the app code[streamlit.py](https://github.com/jarc-101/pokedex/blob/main/streamlit.py) 