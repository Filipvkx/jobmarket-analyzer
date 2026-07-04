from fastapi import FastAPI
from app import models
from app.database import engine

#budowanie tabeli z bazy
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "JobMarket-Analyzer działa jak marzenie xdd"}


    