from typing import Union
from fastapi import FastAPI
import redis
import os
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()
redis_conn = redis.Redis.from_url(os.environ.get('REDIS_HOST_PASSWORD'))

app = FastAPI()


@app.get("/")
def read_root():
    counter = redis_conn.incr('test:increment',1)
    return {"Counter": counter}

@app.get("/counter/{c}")
def counter(c:int):
    counter = redis_conn.incr('test:increment',c)
    return {"Counter": counter}


@app.get("/pico_w/{date}")
async def read_item(date:str ,address:str,celsius:float,light:float):
    #print(f"日期:{date}")
    redis_conn.rpush('pico_w:date',date)
    #print(f"位置:{address}")
    redis_conn.hset('pico_w:address',mapping={date:address})
    #print(f"攝氏:{celsius}")
    redis_conn.hset('pico_w:temperature',mapping={date:celsius})
    #print(f"光線:{light}")
    redis_conn.hset('pico_w:light',mapping={date:light})
    return {"狀態":"儲存成功"}


class Pico_w(BaseModel):
    date:str
    address:str
    temperature:float
    light:float

@app.get("/pico_w/")
async def read_item(count:int=1):
    date_list = redis_conn.lrange('pico_w:date',-count,-1)
    dates = [date.decode() for date in date_list]
    all_Data:[Pico_w] = []
    for date in dates:
        address_get = redis_conn.hget('pico_w:address',date).decode()
        temperature_get = redis_conn.hget('pico_w:temperature',date).decode()
        light_get = redis_conn.hget('pico_w:light',date).decode()
        item = Pico_w(date=date,address=address_get,temperature=float(temperature_get),light=float(light_get))
        all_Data.append(item)

    
    return all_Data