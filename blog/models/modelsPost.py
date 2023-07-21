#BIBLIOTECAS
from sqlalchemy import Column,Integer,String
from blog.infra.sqlalchemy.database import Base

class Post(Base):
    __tablename__= 'post'

    id = 