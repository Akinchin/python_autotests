import requests
import pytest

def test_trainers():
    response = requests.get('https://pokemonbattle.me:9104/trainers')
    assert response.status_code == 200

def test_namepokemon():
    response = requests.get('https://pokemonbattle.me:9104/trainers', params = {'trainer_id' : 3425})
    assert response.json()['trainer_name'] == 'az'