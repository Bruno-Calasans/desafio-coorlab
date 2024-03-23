from fastapi import FastAPI, HTTPException
import json
from src.utils.hoursToInt import hoursToInt
from src.utils.moneyToFloat import moneyToFloat

with open('src/data.json', 'r', encoding='utf-8') as file:
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
def get_travels_by_city(city: str):
    try:
        foundCity = False
        cities = get_city()
        for c in cities:
            if c.lower() == city.lower(): foundCity = True

        if foundCity == False:
            raise HTTPException(404, "City not found")
        
        cityTravels: list[dict[str, str | int]] = []
        for travel in travels:
            if 'city' in travel and travel.get('city').lower() == city.lower():
                cityTravels.append(travel)
        return cityTravels

    except NameError:
        raise HTTPException(500, "Server error")
    
# return the confort and economic travels
@app.get('/best-travels/{city}')
def get_best_travels(city: str):
    try:
        cityTravels = get_travels_by_city(city)
        travelResult = {'confort': None, 'economic': None}

        if len(cityTravels) == 1:
            travelResult.update({'confort': cityTravels[0], 'economic': cityTravels[0]})


        else:
            faster_travel = cityTravels[0]
            econ_travel = cityTravels[1]

            lower_duration = hoursToInt(cityTravels[0].get('duration'))
            lower_price = moneyToFloat(cityTravels[1].get('price_econ'))

            for travel in cityTravels:
                duration = hoursToInt(travel.get('duration'))
                price_confort = moneyToFloat(travel.get('price_confort'))
                price_econ = moneyToFloat(travel.get('price_econ'))
                faster_price_confort = moneyToFloat(faster_travel.get('price_confort'))
                lower_price_econ = moneyToFloat(faster_travel.get('price_confort'))
                
                # getting the faster travel
                if duration < lower_duration:
                    faster_travel = travel

                # getting the conforter travel
                if duration == lower_duration and price_confort > faster_price_confort: 
                    faster_travel = travel

                # getting lower price travel
                if price_econ < lower_price:
                    econ_travel = travel

                # if price_econ == lower_price and lower_price_econ

            travelResult.update({'confort': faster_travel, 'economic': econ_travel})
         
        return travelResult
    
    except NameError:
        raise HTTPException(500, "Server error")