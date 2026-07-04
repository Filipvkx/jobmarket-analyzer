import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

#otwarcie pliku .env z hasłami
load_dotenv()

#wyciągamy hasła do zmiennych
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
POSTGRES_DB = os.getenv("POSTGRES_DB")

#adres URL do bazy w formacie: postgresql://użytkownik:hasło@host:port/nazwa_bazy
SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@localhost:5432/{POSTGRES_DB}"

#inicjujemy silnik, połączenie ze słoniem
engine = create_engine(SQLALCHEMY_DATABASE_URL)

#sesja
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#baza dla przyszłych tabel
Base = declarative_base()
