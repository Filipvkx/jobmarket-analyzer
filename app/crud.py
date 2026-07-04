from sqlalchemy.orm import Session
from app import models, schemas

def create_job_offer(db: Session, offer: schemas.JobOfferCreate):
    db_offer = models.JobOffer(
        title=offer.title,
        company=offer.company,
        location=offer.location,
        salary_min=offer.salary_min,
        salary_max=offer.salary_max,
        url=offer.url
    )
    db.add(db_offer)
    db.commit()
    db.refresh(db_offer)
    return db_offer

def get_job_offers(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.JobOffer).offset(skip).limit(limit).all()

def get_job_offer_by_id(db: Session, offer_id: int):
    return db.query(models.JobOffer).filter(models.JobOffer.id == offer_id).first()

def delete_job_offer_by_id(db: Session,offer_id: int):
    db_offer = db.query(models.JobOffer).filter(models.JobOffer.id == offer_id).first()
    
    if db_offer:
        db.delete(db_offer)
        db.commit()
        return db_offer
    return None
        
