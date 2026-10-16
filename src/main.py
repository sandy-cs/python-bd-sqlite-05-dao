from .model.usuario import Usuario
from .dao.usuario_dao import UsuarioDAO

"""
1) O "-> None" indica que "main()" não retorna um valor útil. 
Em Python, se a função termina sem um return explícito, ela 
retorna "None" automaticamente.

2) A anotação é apenas informativa para ferramentas e leitores; 
não força esse comportamento em tempo de execução. 

3) Em Python, o valor equivalente a "nulo" é "None", não "NULL".
"""

def main() -> None:
    # O DAO concentra o acesso ao banco. O programa usa o métodos sem
    # precisar conhecer os comandos SQL executados internamente.
    usuario_dao = UsuarioDAO()
    usuario_dao.create_table()
    
    '''
    FLUXO 1: 
      CRUD (CREATE, READ, UPDATE, DELETE)
    '''
    
    # CREATE: cadastra o usuário e guarda no objeto o ID gerado pelo SQLite.
    usuario = Usuario(nome = "Ana", nascimento = "2000-06-07")
    usuario = usuario_dao.create(usuario)

    # READ: consulta pelo ID e exibe os dados encontrados.
    usuario_dao.read(usuario.id)

    # UPDATE: altera o objeto e persiste a mudança no banco.
    usuario.nome = "Ana Silva"
    usuario_dao.update(usuario)
    usuario_dao.read(usuario.id)

    # DELETE: remove o registro; a consulta seguinte demonstra que ele não existe mais.
    usuario_dao.delete(usuario)
    usuario_dao.read(usuario.id)

    '''
    FLUXO 2: 
      Cadastro e atualização de outros usuários.
    '''

    # CREATE: cadastra o usuário e guarda no objeto o ID gerado pelo SQLite.
    usuario = Usuario(nome = "Bruna", nascimento = '2006-08-07')
    usuario = usuario_dao.create(usuario)
    usuario_dao.read(usuario.id)

    # UPDATE: altera o objeto e persiste a mudança no banco.
    usuario.nome = "Bruna Gomes"
    usuario_dao.update(usuario)
    usuario_dao.read(usuario.id)

    # CREATE: cadastra o usuário e guarda no objeto o ID gerado pelo SQLite.
    usuario = Usuario(nome = "Carlos", nascimento = "2009-11-15")
    usuario = usuario_dao.create(usuario)
    usuario_dao.read(usuario.id)

    # UPDATE: altera o objeto e persiste a mudança no banco.
    usuario.nome = "Carlos Pereira"
    usuario_dao.update(usuario)
    usuario_dao.read(usuario.id)


# Executa o exemplo apenas quando este módulo é iniciado diretamente.
if __name__ == "__main__":
    main()


'''
OBS:

O bloco:

if __name__ == "__main__":
    main()

1) Faz com que main() seja executada somente quando main.py for 
iniciado diretamente. 

2) Se outro módulo importar main.py, o código não será executado 
automaticamente.

3) Isso é útil para reutilizar ou testar funções do arquivo sem, 
por exemplo, criar tabelas e alterar o banco apenas por causa de 
uma importação. 

4) Neste exemplo, como os imports são relativos (from .model...), 
execute o exemplo pela raiz do projeto com 'python -m src.main'.

5) '__name__' será diferente de "__main__" quando o arquivo for 
importado como módulo, em vez de iniciado como programa principal.

6) No projeto, se outro código fizer:

import src.main

dentro de 'main.py', '__name__' será "src.main". Assim, o bloco 
condicional não chamará 'main()' durante a importação.

7) O valor de '__name__' costuma ser o nome do módulo usado para 
importá-lo, incluindo o pacote quando houver: por exemplo, "src.main" 
ou "src.dao.usuario_dao". Entretanto, ao executar com 'python -m src.main, main.py' 
é tratado como o programa principal e '__name__' será "__main__".


'''