from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# URL de conexão com o PostgreSQL
DATABASE_URL = "postgresql://postgres:lipe1310@localhost:5432/heroi"

# Criação do engine para conectar ao banco de dados
engine = create_engine(DATABASE_URL)

# Criando a sessão que irá fazer a interação com o banco de dados
SessionLocal = sessionmaker(bind=engine)

# Classe base para modelos SQLAlchemy
Base = declarative_base()

# Função para obter uma sessão do banco de dados
def get_db():
    db = SessionLocal()  # Cria a sessão
    try:
        yield db  # Retorna a sessão para uso
    finally:
        db.close()  # Fecha a sessão quando terminar