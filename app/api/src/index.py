from fastapi import FastAPI, HTTPException
import json
from src.utils.hoursToInt import hoursToInt
from src.utils.moneyToFloat import moneyToFloat
from fastapi.middleware.cors import CORSMiddleware

with open('src/data.json', 'r', encoding='utf-8') as file:
    travels: list[dict[str, str | int]] = json.load(file).get('transport')

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
    "http://localhost",
    "http://localhost:8080"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# start end-point
@app.get('/')
def home():
    return {'message': 'api is online'}

# return all the cities
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
    
# return the fast/confortable and economic travels
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
      
            for travel in cityTravels:

                duration = hoursToInt(travel.get('duration'))
                price_confort = moneyToFloat(travel.get('price_confort'))
                price_econ = moneyToFloat(travel.get('price_econ'))

                # faster travel's duration and price
                faster_travel_duration = hoursToInt(faster_travel.get('duration'))
                faster_price_confort = moneyToFloat(faster_travel.get('price_confort'))
                
                 # economic travel's duration and price
                econ_travel_duration = moneyToFloat(econ_travel.get('duration'))
                econ_price_econ = moneyToFloat(econ_travel.get('price_econ'))
                
                # getting the faster travel
                if duration < faster_travel_duration:
                    faster_travel = travel

                # getting the faster and confortable travel
                if duration == faster_travel_duration and price_confort > faster_price_confort: 
                    faster_travel = travel

                # getting the more economic travel
                if price_econ < econ_price_econ:
                    econ_travel = travel

                # getting tthe more economic travel and fast travel
                if price_econ == econ_price_econ and duration < econ_travel_duration:
                    econ_travel = travel

            travelResult.update({'confort': faster_travel, 'economic': econ_travel})
         
        return travelResult
    
    except NameError:
        raise HTTPException(500, "Server error")