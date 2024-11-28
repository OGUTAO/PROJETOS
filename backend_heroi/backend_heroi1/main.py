import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import backend_heroi1.models as models
import backend_heroi1.schemas as schemas
import backend_heroi1.crud as crud
from backend_heroi1.database import SessionLocal
from sqlalchemy import create_engine
from backend_heroi1.database import Base, engine

app = FastAPI()

logging.info("Aplicação iniciada")

def get_db():
    db = SessionLocal()
    try:
        yield db
    except Exception as e:
        print(f"Erro na conexão com o banco de dados: {e}")  
        raise HTTPException(status_code=500, detail=f"Erro na conexão com o banco de dados: {e}") 
    finally:
        db.close()

# Endpoint para testar a conexão com o banco de dados
@app.get("/test-db-connection")
def test_db_connection(db: Session = Depends(get_db)):
    try:
        db.execute("SELECT 1")
        return {"status": "success", "message": "Database connection successful"}
    except Exception as e:
        raise HTTPException(status_code=500, detail="Database connection failed")

# Endpoint para criar um herói
@app.post("/herois/", response_model=schemas.Hero)
def create_hero(hero: schemas.HeroCreate, db: Session = Depends(get_db)):
    return crud.create_heroi(db=db, heroi=hero)

# Endpoint para buscar um herói por ID
@app.get("/herois/{hero_id}", response_model=schemas.Hero)
def read_hero(hero_id: int, db: Session = Depends(get_db)):
    db_hero = crud.get_heroi(db=db, heroi_id=hero_id)
    if db_hero is None:
        raise HTTPException(status_code=404, detail="Hero not found")
    return db_hero

# Endpoint para listar todos os heróis com paginação
@app.get("/herois/", response_model=list[schemas.Hero])
def read_heroes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_herois(db=db, skip=skip, limit=limit)

# Endpoint para atualizar um herói
@app.put("/herois/{hero_id}", response_model=schemas.Hero)
def update_hero(hero_id: int, hero_update: schemas.HeroUpdate, db: Session = Depends(get_db)):
    db_hero = crud.update_heroi(db=db, heroi_id=hero_id, heroi_update=hero_update)
    if db_hero is None:
        raise HTTPException(status_code=404, detail="Hero not found")
    return db_hero

# Endpoint para deletar um herói
@app.delete("/herois/{hero_id}", response_model=schemas.Hero)
def delete_hero(hero_id: int, db: Session = Depends(get_db)):
    db_hero = crud.delete_heroi(db=db, heroi_id=hero_id)
    if db_hero is None:
        raise HTTPException(status_code=404, detail="Hero not found")
    return db_hero

# Endpoint de teste para a raiz "/"
@app.get("/")
def read_root():
    return {"message": "API Funcionando!"}


