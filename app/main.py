from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, crud
from app.database import engine, SessionLocal

#budowanie tabeli z bazy
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

#dependency injection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/offers", response_model=schemas.JobOfferResponse)
def create_offer(offer: schemas.JobOfferCreate, db: Session = Depends(get_db)):
    return crud.create_job_offer(db=db, offer=offer)

@app.get("/offers", response_model=list[schemas.JobOfferResponse])
def read_offers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    offers = crud.get_job_offers(db, skip=skip, limit=limit)
    return offers

@app.get("/offers/{offer_id}", response_model=schemas.JobOfferResponse)
def read_offer(offer_id: int, db: Session = Depends(get_db)):
    db_offer = crud.get_job_offer_by_id(db, offer_id=offer_id)
    if db_offer is None:
        raise HTTPException(status_code=404, detail="Oferta o podanym ID nie istnieje")
    return db_offer
    
@app.delete("/offers/{offer_id}", response_model=schemas.JobOfferResponse)
def delete_offer(offer_id: int, db: Session = Depends(get_db)):
    db_delete_offer = crud.delete_job_offer_by_id(db, offer_id=offer_id)
    if db_delete_offer is None:
        raise HTTPException(status_code=404, detail="Oferta o podanym ID nie istnieje")
    return db_delete_offer

@app.put("/offers/{offer_id}", response_model=schemas.JobOfferResponse)
def update_offer(offer_id: int, offer_data: schemas.JobOfferCreate, db: Session = Depends(get_db)):
    db_update_offer = crud.update_job_offer_by_id(db, offer_id=offer_id, new_offer_data=offer_data)
    if db_update_offer is None:
        raise HTTPException(status_code=404, detail="Oferta o podanym ID nie istnieje")
    return db_update_offer