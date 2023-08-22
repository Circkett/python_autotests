import requests
import pytest

host = 'https://api.pokemonbattle.me:9104'
token = '7b984911b96b9840b2d17198270b65df'

def test_status_code():
    response = requests.get(f'{host}/trainers', params = {'trainer_id': 1804})
    assert response.status_code == 200

def test_part_of_answer():
    response = requests.get(f'{host}/trainers', params = {'trainer_id': 1804})
    assert response.json()['trainer_name'] == 'Trainer1'