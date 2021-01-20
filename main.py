import requests
import random

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import  StaticFiles

app = FastAPI()
templates = Jinja2Templates(directory="templates")
url = 'https://api.adviceslip.com/advice'
personal_quotes = [
    'Если что-то кажется тебе слишком трудным, не думай, что это за пределами сил человека',
    'Начинай уже сейчас жить той жизнью, какой ты хотел бы видеть ее в конце',
    'Надо покорять умом то, что нельзя одолеть силой',
    'Что разум человека может постигнуть и во что он может поверить, того он способен достичь', 
    'Стремитесь не к успеху, а к ценностям, которые он дает​', 
    'Сложнее всего начать действовать, все остальное зависит только от упорства', 'Логика может привести Вас от пункта А к пункту Б, а воображение — куда угодно!']

@app.get("/")
def home_route(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})


@app.get("/give-advice/")
def give_advice(request: Request):
    advice = get_advice_by_url(url)

    if advice:
    	return templates.TemplateResponse("advice.html", {"request": request, "advice": advice})
    else:
        return 'Oopps'

@app.get('/give-advice/{name}')
def give_personal_advice(name):
    advice = get_advice_by_url(url)

    if advice:
        ma_quote = random.choice(personal_quotes)
        return '%s: мой Вам совет на сегодня: %s Цитата для мотивации и вдохновения: %s' % (name.capitalize(), advice, ma_quote)
    else:
        return 'Opps'

def get_advice_by_url(url):
    response = requests.get(url)

    if response.status_code == 200:
        result = response.json()
        advice = result['slip']['advice']

        return advice
    else:
        return False




# import requests
# import random

# from fastapi import FastAPI, Request
# from fastapi.templating import Jinja2Templates

# app = FastAPI()
# templates = Jinja2Templates(directory="templates")
# url = 'https://api.adviceslip.com/advice'

# @app.get("/")
# def home_route(request: Request):
#     return templates.TemplateResponse("main.html", {"request": request})

# @app.get("/give-advice/{name}")
# def give_advice(request: Request, name: str):
#     url = 'https://api.adviceslip.com/advice'
#     response = requests.get(url)

#     if response.status_code == 200:
#         result = response.json()
#         advice = result['slip']['advice']

#         return templates.TemplateResponse("advice.html", {
#             'request': request,
#             'advice': advice, # это переменная advice, которую мы передаем в шаблон
#             'name': name.capitalize() # это переменная name, которую мы передаем в шаблон
#         })
#         # переданные переменные можно использовать в шаблоне обрамив символами {{}}, например {{name}}
#     else:
#         return 'Oopps, something gone wrong!'
