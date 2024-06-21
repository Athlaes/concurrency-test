import json
import logging
import uvicorn

from fastapi import FastAPI
from fastapi.logger import logger


app = FastAPI()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


def read_file(filename: str):
    val = ""
    with open(file=filename, mode="r", encoding="UTF-8") as f:
        val = json.load(f)
    return val


@app.get("/file/open")
def open_file():
    return {"message": value}


@app.get("/hello")
def say_hello():
    return {"message": "hello"}


value = read_file(filename="large-file.json")

uvicorn.run(app, host="localhost", port=8080)
