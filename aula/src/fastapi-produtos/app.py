from fastapi import FastAPI, Request, HTTPException
from models.product import Product

from datetime import datetime
from pytz import timezone

import uuid

app = FastAPI()

data = []


# Default
@app.get("/")
async def default():
    return [
        {
    "Bem-vindo": "Bem-vindo à nossa incrível API! Aqui você pode encontrar uma variedade de itens e explorar suas características.",
    "Como começar": {
        "Explorar itens": "Para começar a explorar os itens, você pode visitar nosso endpoint de itens em 'localhost:8000/items'.",
        "Documentação": "Se você precisar de mais informações sobre como usar nossa API, confira nossa documentação completa em 'localhost:8000/docs'.",
        "Suporte": "Se você tiver alguma dúvida ou encontrar algum problema, basta nos contatar!"
    },
    "Obrigado": "Agradeço por escolher nossa API e esperamos que você tenha uma ótima experiência!"
}
    ]

# CREATE - POST
@app.post("/items/")
async def create_item(item: Product):
    horario_de_brasilia = timezone('America/Sao_Paulo')
    item.created_at = datetime.now(horario_de_brasilia).strftime("%Y-%m-%dT%H:%M:%S")

    item.id = str(uuid.uuid4())
    item.price = f"{round(item.price, 2):.2f}"

    if any(existing_item.id == item.id for existing_item in data):
        return {"error": "Item with this ID already exists"}
    data.append(item)
    return {"message": "Sucess", "Registered Item": item}

# READ - GET
@app.get("/items")
async def read_items(request: Request):
    if not data:
        raise HTTPException(status_code=404, detail="ID not found")
    for item in data:
        item.link_id = [{"href": f"{str(request.url)}/{item.id}"}]
    return {"message": "Sucess", "Itens": data}

@app.get("/items/{item_id}")
async def read_item(item_id: str):
    for item in data:
        if item.id == item_id:
            return {"message":"Sucess", "Item":item}
    raise HTTPException(status_code=404, detail="ID not found")

# UPDATE - PUT
@app.put("/items/{item_id}")
async def update_item(item_id: str, item: Product):
    for index, current_item in enumerate(data):
        if current_item.id == item_id:

            updated_item = data[index]
            updated_item.name = item.name
            updated_item.description = item.description
            updated_item.price = item.price

            
            return {"message": "Item update", "item": update_item}
    raise HTTPException(status_code=404, detail="ID not found")

# DELETE - DELETE
@app.delete("/items/{item_id}")
async def delete_item(item_id: str):
    for index, current_item in enumerate(data):
        if current_item.id == item_id:
            item_to_delete = data[index]
            del data[index]
            return {"message": "Item deleted", "item": item_to_delete}
    raise HTTPException(status_code=404, detail="ID not found")