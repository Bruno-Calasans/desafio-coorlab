from fastapi import FastAPI
import json

with open('src/data.json', 'r') as file:
    travels: list[dict[str, str | int]] = json.load(file).get('transport')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'hello'}

@app.get('/cities')
def getCities():
    cities: set[str] = set()

    for travel in travels:
        if 'city' in travel:
            cities.add(travel.get('city'))

    return cities
        