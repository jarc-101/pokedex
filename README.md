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

## Solution 
![alt text](https://github.com/jarc-101/pokedex/blob/main/image/result_six_pokemon.png)

See full code with comments : [pokedex.py](https://github.com/jarc-101/pokedex/blob/main/six_pokemon.py)


### I also created an app using streamlit to explore python more
Here's the app code: [streamlit.py](https://github.com/jarc-101/pokedex/blob/main/streamlit.py)

![alt text](https://github.com/jarc-101/pokedex/blob/main/image/streamlit_pokedex.png)

## Try my APP here !! 
[pokedex_app](https://pokedex-py.streamlit.app/)
