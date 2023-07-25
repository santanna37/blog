#BIBLIOTECAS
from sqlalchemy import Column,Integer,String
from blog.infra.sqlalchemy.database import Base

#MODELOS USUARIOS

class Usuario(Base):
    __tablename__='usuarios'
    
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    nome = Column(String)
    email = Column(String)
    senha = Column(String)
    