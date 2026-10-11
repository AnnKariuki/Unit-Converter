from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/length")
def length_page(request: Request):
    return templates.TemplateResponse(request, "length.html", {"title": "length"})

@app.get("/temperature")
def temperature_page(request: Request):
    return templates.TemplateResponse(request, "temperature.html", {"title": "temperature"})

@app.get("/weight")
def weight_page(request: Request):
    return templates.TemplateResponse(request, "weight.html", {"title": "weight"})


@app.post('/length')
def convert_length(request:Request):
    print(request.body)
    pass

