# BLIBLIOTECAS
from pydantic import BaseModel
from typing import Optional 

# SCHEMAS DE USUARIOS 

class Usuario(BaseModel):
    id: Optional[str] = None
    nome: str
    email: str
    senha: str
    
    class config:
        orm_mode=True

class AlterarUsuario(Usuario):
    id: Usuario.id
    nome: str
    email: str
    senha: str

