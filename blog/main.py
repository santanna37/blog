from fastapi import FastAPI, Depends, status
from sqlalchemy.orm import Session
from blog.infra.sqlalchemy.database import criar_db
from blog.routers import routersUsuario


# PRINCIPAL 

#CLIRANDO BANCO DE DADOS

criar_db()
app = FastAPI()

# ROTAS 
app.include_router(routersUsuario.router)

