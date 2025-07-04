from fastapi import FastAPI
from enum import Enum


app = FastAPI()


class FoodItems(str,Enum):
    indian = 'indian'
    pakistani = 'pakistani'
    thai = 'thai'



coupon_codes = {
    1 : '10%',
    2 : '20%',
    3: '30%'
}


food_items = {
    'indian' : ['samosa' ,' pakoray'],
    'pakistani' : ['poori', ' halwa'],
    'thai' : ['chicken' ,' shrimps'],
}

@app.get("/welcome/{name}")
async def welcome(name):
    return f"welcome {name}"


@app.get("/get_discount/{coupon_code}")
async def get_discount(coupon_code : int):
    return coupon_codes.get(coupon_code)


@app.get("/get_items/{item}")
async def get_items(item: FoodItems):
    return food_items.get(item)[0]