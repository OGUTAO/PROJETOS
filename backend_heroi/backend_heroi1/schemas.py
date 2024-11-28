from pydantic import BaseModel
from typing import Optional
from datetime import date

class HeroBase(BaseModel):
    nome: str
    alias: str
    descricao: str
    cidade: str
    altura: Optional[float] = None  # Novo campo
    sexo: Optional[str] = None  # Novo campo
    peso: Optional[float] = None  # Novo campo
    data_nascimento: Optional[date] = None  # Novo campo
    nome_real: Optional[str] = None  # Novo campo
    local_nascimento: Optional[str] = None  # Novo campo
    nivel_de_forca: Optional[int] = None  # Novo campo
    status: Optional[str] = None  # Novo campo

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
    altura: Optional[float] = None
    sexo: Optional[str] = None
    peso: Optional[float] = None
    data_nascimento: Optional[date] = None
    nome_real: Optional[str] = None
    local_nascimento: Optional[str] = None
    nivel_de_forca: Optional[int] = None
    status: Optional[str] = None

class Hero(HeroBase):
    id: int

    class Config:
        from_attributes = True
