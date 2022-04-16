from sanic import Sanic
from sanic.response import json, text

from data import SUPPORTED_CATEGORIES, FILTERS

app = Sanic("Pricify")

@app.get("/")
async def index(request):
    return text("Pricify API says hello!") 

@app.get("/category")
async def get_categories(request):
    return json(SUPPORTED_CATEGORIES)

@app.get("/filters/<category_id>")
async def get_filters(request, category_id):
    return json(FILTERS[category_id])

@app.post("/get_result")
async def generate_result(request):
    data = request.json
    engine = data["engine"]
    mileage = data["mileage"]
    seats = data["seats"]
    vehicle_age = data["vehicle_age"]
    km_driven = data["km_driven"]
    max_power = data["max_power"]
    brand = data["brand"]
    model = data["model"]
    fuel_type = data["fuel_type"]

    res = gen_result()

    return json(res)
