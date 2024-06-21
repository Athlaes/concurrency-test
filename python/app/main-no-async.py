import json
import logging
import uvicorn

from fastapi import FastAPI
from fastapi.logger import logger

app = FastAPI()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


def read_file(filename: str):
    value = ""
    with open(file=filename, mode="r", encoding="UTF-8") as f:
        value = json.load(f)
    return value


@app.get("/file/open")
def open_file():
    value = ""
    logger.info(msg="Starting file opening")
    value = read_file(filename="large-file.json")
    logger.info(msg="End of file opening")
    return {"message": value}


@app.get("/hello")
def say_hello():
    return {"message": "hello"}


uvicorn.run(app, host="localhost", port=8080)
