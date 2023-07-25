# BIBLIOTECAS
from sqlalchemy.orm import Session
from blog.schemas import schemaUsuario
from blog.models import modelsUsuario 
from sqlalchemy import *


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
    

    def listar(self):
        lista = select(modelsUsuario.Usuario)
        usuarios = self.session.execute(lista).scalars().all()
        return usuarios


    def editar( self, email: str, usuario: schemaUsuario.AlterarUsuario):
        updateConta = update(
                        modelsUsuario.Usuario).where(
                                                    modelsUsuario.Usuario.email == email
                                                    ).values(
                                                            nome = usuario.nome,
                                                            email = usuario.email,
                                                            senha = usuario.senha
                                                            )
        
        self.session.execute(updateConta)
        self.session.commit()
        



    # def editar(self, id: int, produto: schemas.Produto):
    #         update_stmt = update(models.Produto).where(
    #             models.Produto.id == id).values(nome=produto.nome,
    #                                             detalhes=produto.detalhes,
    #                                             preco=produto.preco,
    #                                             disponivel=produto.disponivel,
    #                                             )
    #         self.session.execute(update_stmt)
    #         self.session.commit()