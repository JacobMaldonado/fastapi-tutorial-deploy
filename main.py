from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


class Persona(BaseModel):
    id: str
    nombre: str

persona = Persona(id="1", nombre="Juan")

@app.get("/")
async def ruta():
    """Hola esto es una documentación"""
    return {"message": "Hola mundo"}

@app.get("/objeto/{objeto_id}")
def ruta_con_parametro(
        objeto_id: int, #valor de la ruta
        q: Optional[str] = None # Parametro de la ruta
    ):
    print(objeto_id)
    print(q)
    return {"objeto_id": objeto_id}

@app.get("/persona/", response_model=Persona)
def ruta_con_modelo():
    return persona

@app.post("/persona/", response_model=Persona)
def ruta_con_modelo_post(nueva_persona: Persona):
    global persona
    persona = nueva_persona
    return persona
