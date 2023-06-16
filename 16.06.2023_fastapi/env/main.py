from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class MyDict(BaseModel):
    key1: str
    key2: str

@app.post('/home')
async def handle_request(data: MyDict):

    print(data.key1)
    print(data.key2)

    return {'message': 'Success'}