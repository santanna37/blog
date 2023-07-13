# BIBLIOTECAS
from sqlalchemy.orm import Session
from blog.schemas import schemaUsuario
from blog.models import modelsUsuario 


# CRIANDO REPOSITORIO 

class RepositorioUsuario():
    def __init__(self, session:Session):
        self.session = session
        
    def criar(self, usuario:schemaUsuario.Usuario):
        db_usuario = modelsUsuario.Usuario(
            id = usuario.id,
            nome = usuario.nome,
            email = usuario.email,
            senha = usuario.senha            
        )
        self.session.add(db_usuario)
        self.session.commit()
        self.session.refresh(db_usuario)
        return db_usuario
    
    def editar ():
        pass