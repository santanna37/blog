# BLIBLIOTECAS
from pydantic import BaseModel
from typing import Optional 

# SCHEMAS DE USUARIOS 


#SCHEMA PRINCIPAL USUARIOS
class Usuario(BaseModel):
    id: Optional[int] = None
    nome: str
    email: str
    senha: str
    
    class config:
        orm_mode = True




# SCHEMA DE RESPOSTA
class UsuarioResposta(BaseModel):
    nome: str
    email: str

    class config:
        orm_mode = True


class AlterarUsuario(BaseModel):
    nome: Optional[str]
    email: Optional[str]
    senha: Optional[str]
    
    class config:
        orm_mode = True
