import json
import logging
import uvicorn
import orjson

from fastapi import FastAPI
from fastapi.logger import logger


app = FastAPI()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


def read_file(filename: str):
    val = ""
    with open(file=filename, mode="r", encoding="UTF-8") as f:
        val = orjson.loads(f.read())
    return val


@app.get("/file/open")
def open_file():
    return orjson.dumps({"message": value})


@app.get("/hello")
def say_hello():
    return orjson.dumps({"message": "hello"})


value = read_file(filename="large-file.json")

uvicorn.run(app, host="localhost", port=8080)
