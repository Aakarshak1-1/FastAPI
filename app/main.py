from fastapi import FastAPI
from app.api.endpoints import items, users
from app.db.session import engine
from app.db.base import Base

app = FastAPI()

app.include_router(items.router, prefix="/items", tags=["items"])
app.include_router(users.router, prefix="/users", tags=["users"])

@app.get("/")
async def root():
    return {"message": "Welcome to the FastAPI application!"}
