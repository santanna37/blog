from passlib.context import CryptContext

pwd = CryptContext(schemes=['bcrypt'])


def gerar_hash(texto):
    return pwd.hash(texto)

def verificar(texto,hashed):
    return pwd.verify(texto,hashed)

