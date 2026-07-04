from sqlalchemy import Column, Integer, String, Boolean
from app.database import Base

class JobOffer(Base):
    __tablename__ = "job_offers"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    company = Column(String, index=True)
    location = Column(String)
    salary_min = Column(Integer, nullable=True) #nullable ponieważ nie zawsze widełki musza być podane
    salary_max = Column(Integer, nullable=True)
    url = Column(String, unique=True)
    requirements = Column(String, nullable=True)
    is_remote = Column(Boolean, default=False)


