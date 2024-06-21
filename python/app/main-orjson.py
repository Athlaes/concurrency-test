import json
import logging
import aiofiles
import uvicorn
import orjson

from fastapi import FastAPI
from fastapi.logger import logger

app = FastAPI()
logger.setLevel(logging.INFO)
logger.addHandler(logging.StreamHandler())


async def read_file(filename: str):
    value = ""
    async with aiofiles.open(file=filename, mode="r", encoding="UTF-8") as f:
        content = await f.read()
        value = orjson.loads(content)
    return value


@app.get("/file/open")
async def open_file():
    value = ""
    logger.info(msg="Starting file opening")
    value = await read_file(filename="large-file.json")
    logger.info(msg="End of2 file opening")
    return orjson.dumps({"message": value})


@app.get("/hello")
def say_hello():
    return orjson.dumps({"message": "hello"})


uvicorn.run(app, host="localhost", port=8080)
