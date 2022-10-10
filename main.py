from fastapi import FastAPI
import uvicorn
from sqlmodel import create_engine
from models.gem_models import *

app = FastAPI()
engine = create_engine("sqlite:///database.db", echo=True)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


@app.get("/")
async def hi():
    return "Hi, dude"


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
    create_db_and_tables()
