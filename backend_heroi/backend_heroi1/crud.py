from sqlalchemy.orm import Session
from . import models, schemas
from fastapi import HTTPException

# Função para buscar heróis no banco de dados
def get_herois(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Heroi).offset(skip).limit(limit).all()

# Função para criar um herói no banco de dados
def create_heroi(db: Session, heroi: schemas.HeroCreate):
    db_heroi = models.Heroi(
        nome=heroi.nome, 
        alias=heroi.alias,
        descricao=heroi.descricao,
        cidade=heroi.cidade
    )
    db.add(db_heroi)
    db.commit()
    db.refresh(db_heroi)
    return db_heroi

# Função para buscar herói por ID
def get_heroi(db: Session, heroi_id: int):
    return db.query(models.Heroi).filter(models.Heroi.id == heroi_id).first()

# Função para atualizar herói
def update_heroi(db: Session, heroi_id: int, heroi_update: schemas.HeroUpdate):
    db_heroi = db.query(models.Heroi).filter(models.Heroi.id == heroi_id).first()
    if db_heroi is None:
        raise HTTPException(status_code=404, detail="Hero not found")

    for key, value in heroi_update.dict(exclude_unset=True).items():
        setattr(db_heroi, key, value)
    
    db.commit()
    db.refresh(db_heroi)
    return db_heroi

# Função para deletar herói
def delete_heroi(db: Session, heroi_id: int):
    db_heroi = db.query(models.Heroi).filter(models.Heroi.id == heroi_id).first()
    if db_heroi is None:
        raise HTTPException(status_code=404, detail="Hero not found")

    db.delete(db_heroi)
    db.commit()
    return db_heroi
