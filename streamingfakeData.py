import random
from fastapi import FastAPI
import time
from fastapi.responses import StreamingResponse
import json

app = FastAPI()

def fakeStream():
    yield json.dumps(str(random.uniform(0, 1))) + "\n"  # Simulate sensor readings
    time.sleep(5)


@app.get("/")
async def sendStream():
    return StreamingResponse(fakeStream())

