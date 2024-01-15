from typing import Union
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

data_base = []

class event(BaseModel):
    nome: str
    dono: str
    descricao : str
    data :str
    quantidade_ingresos: int
    foi_vendido: bool
    data_validade :int 

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/event",response_model = Events)
async def criar_eventos(event: Events):
    data_base.append(event)
    
    return event
@app.get('/event')

async def ler_events() -> List[event]:
    return data_base