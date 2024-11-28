from sqlalchemy import Column, Integer, String
from .database import Base

# Modelo da tabela Heroi
class Heroi(Base):
    __tablename__ = "herois"  # Nome da tabela no banco de dados

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)  # Indexando para melhorar performance em buscas por nome
    alias = Column(String, index=True)  # Se você quiser buscar frequentemente por alias
    descricao = Column(String)
    cidade = Column(String)
