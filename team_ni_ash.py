import requests
import sys
import random


def search_pokemon(name):
  response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}/")
  pokemon = response.json()
  add_pokemon(pokemon)

def add_pokemon(pokemon):
  Name = f"Name: {pokemon['name'].capitalize()}"
  hp = f"HP: {pokemon['stats'][0]['base_stat']}"
  items = f"Held Items: {pokemon['held_items']}"

  if len(pokemon['held_items']) == 0:
    items_print = "Held Item: No item held"
  else:
    items = [item['item']['name'] for item in pokemon['held_items']]
    items = random.sample(items,1)
    items_print = f"Held Item: {items[0]}"

  print(Name)
  print(hp)
  print(items_print)
  get_moves(pokemon)

def get_moves(pokemon):
  moves = [move['move']['name'] for move in pokemon['moves']]
  moveset = random.sample(moves,4)
  print(f"Moveset: {moveset[0]}, {moveset[1]}, {moveset[2]}, {moveset[3]}\n")

if __name__ == "__main__":  
  # choose_you()
  search_pokemon(sys.argv[1])
  search_pokemon(sys.argv[2])
  search_pokemon(sys.argv[3])
  search_pokemon(sys.argv[4])
  search_pokemon(sys.argv[5])
  search_pokemon(sys.argv[6])




  poke_num = 0
  team = {}
  while poke_num != 6:
    poke_name = input("Choose your Pokemon: ").capitalize()
    team[poke_name] = "1"
    poke_num +=1
  print(team)
