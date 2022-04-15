from sanic import Sanic
from sanic.response import json

app = Sanic("Pricify")

@app.get("/")
async def index(request):
    return text("Pricify API says hello!") 

# TODO: the actual API endpoints
