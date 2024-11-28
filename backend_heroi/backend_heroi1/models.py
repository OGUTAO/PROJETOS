from sqlalchemy import Column, Integer, String, Float, Date
from .database import Base

# Modelo da tabela Heroi
class Heroi(Base):
    __tablename__ = "herois"  # Nome da tabela no banco de dados

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, index=True)  # Indexando para melhorar performance em buscas por nome
    alias = Column(String, index=True)  # Se você quiser buscar frequentemente por alias
    descricao = Column(String)
    cidade = Column(String)
    altura = Column(Float)  # Coluna para altura (tipo float para medidas decimais)
    sexo = Column(String)  # Coluna para sexo (tipo string, ajustável para 'M', 'F' ou outros)
    peso = Column(Float)  # Coluna para peso (tipo float para medidas decimais)
    data_nascimento = Column(Date)  # Coluna para data de nascimento (tipo Date)
    nome_real = Column(String)  # Nome real do herói
    local_nascimento = Column(String)  # Local de nascimento
    fk_poderes_poderes_pk = Column(Integer)  # Referência para a tabela de poderes
    nivel_de_forca = Column(Integer)  # Nível de força do herói
    status = Column(String)  # Status do herói (ex: 'ativo', 'inativo', etc.)
    fk_historico_de_batalhas_pk = Column(Integer)  # Referência para a tabela de histórico de batalhas
