import hashlib

def encrypt_password(password: str) -> str:
    """
    Converte a string da senha, informada no formulário de autenticação, para o padrão do banco de dados Sig
    :param password: string
    :return: string da senha em hex md5
    """
    return hashlib.md5(password.encode('utf')).hexdigest()
