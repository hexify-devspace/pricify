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
