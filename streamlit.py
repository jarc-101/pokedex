import streamlit as st
import requests
import random,time


@st.cache_data(show_spinner = "Throwing Pokeballs:man-playing-handball:....:red_circle::red_circle:")

def search_pokemon(name):
  response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}/")
  pokemon = response.json()

  col1, col2 = st.columns(2)
  with col1:
    get_img(pokemon)
  with col2:
    print_pokemon(pokemon)

def print_pokemon(pokemon):
  st.write(f"Name: {pokemon['name'].capitalize()}")
  st.write(f"ID: {pokemon['id']}")
  st.write(f"Base XP: {pokemon['base_experience']}")
  st.write(f"HP: {pokemon['stats'][0]['base_stat']}")
  add_items(pokemon)

def add_items(pokemon):
  items = f"Held Items: {pokemon['held_items']}"
  if len(pokemon['held_items']) == 0:
    items_print = "Held Item: No item held"
  else:
    items = [item['item']['name'] for item in pokemon['held_items']]
    items = random.sample(items,1)
    items_print = f"Held Item: {items[0]}"
  st.write(items_print)
  get_moves(pokemon)

def get_moves(pokemon):
  moves = [move['move']['name'] for move in pokemon['moves']]
  moveset = random.sample(moves,4)
  st.write(f"Moveset: {moveset[0]}, {moveset[1]}, {moveset[2]}, {moveset[3]}\n")

def get_img(pokemon):
  try:
    img_url = pokemon['sprites']['other']['dream_world']['front_default']
    st.image(img_url,use_column_width="auto")
  except:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/Pok%C3%A9_Ball_icon.svg/770px-Pok%C3%A9_Ball_icon.svg.png",use_column_width="auto")
    # st.write("No image available yet")


st.title("Pokedex")
try:
  name = st.text_input('A wild Pokemon has appeared')
  chosen = search_pokemon(name.lower())

except:
  if len(name) >= 1:
    st.write("Please input a valid Pokemon name")
    msg = st.toast("Please input a valid Pokemon name!")
    time.sleep(1)
  else:
    pass

