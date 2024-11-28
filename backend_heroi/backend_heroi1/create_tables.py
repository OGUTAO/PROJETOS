from sqlalchemy import create_engine
from models import Base  # Importando o Base, onde os modelos são definidos

engine = create_engine("postgresql://postgres:lipe1310@localhost:5432/heroi")
Base.metadata.create_all(bind=engine)
