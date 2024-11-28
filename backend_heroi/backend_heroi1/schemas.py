from pydantic import BaseModel
from typing import Optional

class HeroBase(BaseModel):
    nome: str
    alias: str
    descricao: str
    cidade: str

    class Config:
        from_attributes = True

# HeroCreate sem validações adicionais
class HeroCreate(HeroBase):
    nome: str
    alias: str
    descricao: str  # Sem a validação de comprimento

# HeroUpdate com campos opcionais
class HeroUpdate(HeroBase):
    nome: Optional[str] = None
    alias: Optional[str] = None
    descricao: Optional[str] = None
    cidade: Optional[str] = None

class Hero(HeroBase):
    id: int

    class Config:
        from_attributes = True
