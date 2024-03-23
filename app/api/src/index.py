from fastapi import FastAPI, HTTPException
import json

with open('src/data.json', 'r') as file:
    travels: list[dict[str, str | int]] = json.load(file).get('transport')

app = FastAPI()

@app.get('/')
def home():
    return {'message': 'hello'}

@app.get('/city')
def get_city():
    try:
        cities: set[str] = set()
        for travel in travels:
            if 'city' in travel:
                cities.add(travel.get('city'))
        return cities
    except:
        raise HTTPException(500, "Server error")

# return all avaliable travels in that city
@app.get('/travel/{city}')
def get_travel_by_city(city: str):
    try:
        foundCity = False
        cities = get_city()
        for c in cities:
            print(c)
            if c.lower() == city.lower(): foundCity = True

        if foundCity == False:
            raise HTTPException(404, "City not found")
        
        cityTravels = []
        for travel in travels:
            if 'city' in travel and travel.get('city').lower() == city.lower():
                cityTravels.append(travel)
        return cityTravels

    except KeyError:
        raise HTTPException(500, "Server error")