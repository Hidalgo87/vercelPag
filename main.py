from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "¡Bienvenido a la API genérica!"}

@app.get("/items/")
async def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit, "items": ["item1", "item2", "item3"]}

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id, "name": f"User {user_id}"}

@app.post("/items/")
async def create_item(item: dict):
    return {"item": item, "status": "creado"}

@app.put("/items/{item_id}")
async def update_item(item_id: int, item: dict):
    return {"item_id": item_id, "item": item, "status": "actualizado"}

@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    return {"item_id": item_id, "status": "eliminado"}

# Agrega más rutas según sea necesario para pruebas.
