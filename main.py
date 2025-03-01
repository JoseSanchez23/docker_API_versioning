from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uuid

app = FastAPI()

# Base de datos en memoria
messages = {}

# Modelo de datos
class Message(BaseModel):
    text: str

@app.post("/messages")
async def create_message(message: Message):
    message_id = str(uuid.uuid4())  # Genera un ID único
    messages[message_id] = {"text": message.text}
    return {"message": "Mensaje guardado", "id": message_id}

@app.get("/messages/{message_id}")
async def get_message(message_id: str):
    message = messages.get(message_id)
    if not message:
        raise HTTPException(status_code=404, detail="Mensaje no encontrado")
    return message

