from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import requests
import math
import random



def index(request):

    num = random.randint(1,800)

    base_pokemon = requests.get(f'https://pokeapi.co/api/v2/pokemon/{num}').json()
    base_pokemon_name = base_pokemon['name']
    image_url = base_pokemon['sprites']['front_default']
    base_pokemon_type = requests.get(base_pokemon['types'][0]['type']['url']).json()
    #base_pokemon_type['pokemon'][0]['pokemon']['name']
    
    random_pokemon = []
    for i in range(5):
        random_num = random.randint(0,len(base_pokemon_type['pokemon'])-1)
        random_pokemon.append(base_pokemon_type['pokemon'][random_num]['pokemon'])

    random_names = []
    for pokemon in random_pokemon:
        url = requests.get(f'{pokemon["url"]}').json()
        random_url = url['sprites']['front_default']
        test = pokemon['name'],random_url
        random_names.append(test)

    pokemon = {
        'image': image_url,
        'base_pokemon_name': base_pokemon_name,
        'base_type_name': base_pokemon['types'][0]['type']['name'],
        'random_pokemon': random_pokemon,
        'random_names': random_names
    }
    return render(request, 'index.html', pokemon)

def search(request, name):

    base_pokemon = requests.get(f'https://pokeapi.co/api/v2/pokemon/{name}').json()
    base_pokemon_name = base_pokemon['name']
    image_url = base_pokemon['sprites']['front_default']
    base_pokemon_type = requests.get(base_pokemon['types'][0]['type']['url']).json()
    
    random_pokemon = []
    for i in range(5):
        random_num = random.randint(0,len(base_pokemon_type['pokemon'])-1)
        random_pokemon.append(base_pokemon_type['pokemon'][random_num]['pokemon'])

    random_names = []
    for pokemon in random_pokemon:
        url = requests.get(f'{pokemon["url"]}').json()
        random_url = url['sprites']['front_default']
        test = pokemon['name'],random_url
        random_names.append(test)

    pokemon = {
        'image': image_url,
        'base_pokemon_name': base_pokemon_name,
        'base_type_name': base_pokemon['types'][0]['type']['name'],
        'random_pokemon': random_pokemon,
        'random_names': random_names
    }
    return render(request, 'index.html', pokemon)

