# BIBLIOTECAS
from fastapi import APIRouter, Depends
from blog.schemas import schemaUsuario  
from sqlalchemy.orm import Session
from blog.repositorios.repositorioUsuario import RepositorioUsuario
from blog.infra.sqlalchemy.database import get_db


#CRIANDO ROTAS DO USUARIO
router = APIRouter()

@router.post('/criar')
def criar_usuario(usuario:schemaUsuario.Usuario, session:Session = Depends(get_db)):
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado