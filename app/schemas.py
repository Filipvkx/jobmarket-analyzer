from pydantic import BaseModel
from typing import Optional

#co wysyła użytkownik
class JobOfferCreate(BaseModel):
    title: str
    company: str
    location: str
    salary_min: Optional[int] = None
    salary_max: Optional[int] = None
    url = str

#co nasze API zwraca
class JobOfferResponse(JobOfferCreate):
    id: int

    class Config:
        from_attributes = True

