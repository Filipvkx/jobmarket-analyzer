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