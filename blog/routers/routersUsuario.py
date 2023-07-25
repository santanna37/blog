# BIBLIOTECAS
from fastapi import APIRouter, Depends
from blog.schemas import schemaUsuario  
from sqlalchemy.orm import Session
from blog.repositorios.repositorioUsuario import RepositorioUsuario
from blog.infra.sqlalchemy.database import get_db
from blog.models.modelsUsuario import Usuario
from sqlalchemy import update
# BIBLIOTECAS DE CRIPTOGRAFICA
from blog.infra.providers import hash_provider



#CRIANDO ROTAS DO USUARIO
router = APIRouter()



# ROTAS

# CRIAR USUARIO
@router.post('/usuario', response_model=schemaUsuario.Usuario)
def criar_usuario(usuario: schemaUsuario.Usuario,
                   session: Session = Depends(get_db)):

    # CRIPTOGRAFIA DE SENHA 
    usuario.senha = hash_provider.gerar_hash(usuario.senha)

    # CRIAR USUARIO
    usuario_criado = RepositorioUsuario(session).criar(usuario)
    return usuario_criado



# LISTAR USUARIOS 
@router.get('/usuarios')
def listar_usuarios(session: Session = Depends(get_db)):
    usuarios = RepositorioUsuario(session).listar()
    return usuarios



# EDITAR USUARIO
@router.put('/usuario/{email}')
def editar_usuario(email, usuario: schemaUsuario.AlterarUsuario,
                   session: Session = Depends(get_db)):

    RepositorioUsuario(session).editar(email,usuario)
  #  email = Usuario.email

    return f'o usuario {usuario.nome} foi atualizado'