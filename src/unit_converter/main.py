from fastapi import FastAPI, Request, Depends, status, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from typing import Annotated
from starlette.datastructures import FormData
app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


async def get_body(request: Request):
    # request.body is a method, not the actual request body. we are just printing a reference to the method itself, not calling it.
    # print(request.body)
    # FastAPI's Request.body() is asynchronous. It reads the incoming HTTP request body, which may involve waiting for data.

    # our html form sends data as application/x-www-form-urlencoded by default. request.form() parses submitted HTML form fields into a FormData object.
    content_type = request.headers.get("content-type")
    if content_type is None:
        raise HTTPException(status_code=400, detail="Invalid form data")
    elif content_type == 'application/x-www-form-urlencoded':
        try:
            return await request.form()
        except Exception:
            raise HTTPException(status_code=400, detail='Invalid Form data')
    else:
        raise HTTPException(status_code=400, detail='Content-Type not supported!')

body_dep = Annotated[FormData, Depends(get_body)]

# how many of unit fit into 1 meter 
length_factors = {
    "millimeter": 1000,
    "centimeter": 100,
    "meter": 1,
    "kilometer": 0.001,
    "inch": 39.3701,
    "foot": 3.28084,
    "yard": 1.09361,
    "mile": 0.000621371
}

# how many of unit fit into 1 gram 
weight_factors = {
    "milligram":1000,
    "gram":1,
    "kilogram":0.001,
    "ounce":0.035274,
    "pound":0.00220462
}
# how many of unit fit into 1 celcius 
temperature_factors = {
    "kelvin":274.15,
    "fahrenheit":33.8,
    "celsius":1,
}

@app.get("/")
def home_page(request: Request): # path operation function
    return templates.TemplateResponse(request, "layouts.html")
@app.get("/length")
def length_page(request: Request):
    return templates.TemplateResponse(request, "length.html", {"title": "length", "converted": False})

@app.get("/temperature")
def temperature_page(request: Request):
    return templates.TemplateResponse(request, "temperature.html", {"title": "temperature",  "converted": False})

@app.get("/weight")
def weight_page(request: Request):
    return templates.TemplateResponse(request, "weight.html", {"title": "weight", "converted": False})


@app.post('/length')
async def convert_length(request: Request, body: body_dep):
    length_str = body["length"]
    from_unit_str = body["from_unit"]
    to_unit_str = body["to_unit"]
    try: 
        # this is for mypy to differentiate between str and FileUpload
        if isinstance(length_str, str) and isinstance(from_unit_str, str) and isinstance(to_unit_str, str):
            length = float(length_str)
            from_unit = from_unit_str
            to_unit = to_unit_str
    except Exception:
        raise HTTPException(status_code=400, detail='Invalid Form data')
    # change from_unit to meters
    value_in_meters = length / length_factors[from_unit] 
    converted_value = value_in_meters * length_factors[to_unit]
    return templates.TemplateResponse(request, "length.html", {"title": "length", "converted": True, "length": length, "from_unit":from_unit, "to_unit": to_unit, "converted_value": converted_value})
    

@app.post('/weight')
async def convert_weight(request: Request, body: body_dep):
    weight_str = body["weight"]
    from_unit_str = body["from_unit"]
    to_unit_str = body["to_unit"]
    try: 
        if isinstance(weight_str, str) and isinstance(from_unit_str, str) and isinstance(to_unit_str, str):
            weight = float(weight_str)
            from_unit = from_unit_str
            to_unit = to_unit_str
    except Exception:
        raise HTTPException(status_code=400, detail='Invalid Form data')
    # change from_unit to grams
    value_in_grams = weight / weight_factors[from_unit] 
    converted_value = value_in_grams * weight_factors[to_unit]
    return templates.TemplateResponse(request, "weight.html", {"title": "weight", "converted": True, "weight": weight, "from_unit":from_unit, "to_unit": to_unit, "converted_value": converted_value})
    

@app.post('/temperature')
async def convert_temprature(request: Request, body: body_dep):
    temperature_str = body["temperature"]
    from_unit_str = body["from_unit"]
    to_unit_str = body["to_unit"]
    try: 
        if isinstance(temperature_str, str) and isinstance(from_unit_str, str) and isinstance(to_unit_str, str):
            temperature = float(temperature_str)
            from_unit = from_unit_str
            to_unit = to_unit_str
    except Exception:
        raise HTTPException(status_code=400, detail='Invalid Form data')
    # change from_unit to celcius
    value_in_celcius = temperature / temperature_factors[from_unit] 
    converted_value = value_in_celcius * temperature_factors[to_unit]
    return templates.TemplateResponse(request, "temperature.html", {"title": "temperature", "converted": True, "temperature": temperature, "from_unit":from_unit, "to_unit": to_unit, "converted_value": converted_value})
    