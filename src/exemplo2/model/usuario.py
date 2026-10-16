from dataclasses import dataclass
from typing import Optional

'''
1) Em Python, 'Optional' é usado nas anotações de tipo para indicar 
   que um valor pode ser de um certo tipo ou pode ser 'None'.

Exemplo:

from typing import Optional
nome: Optional[str] = None

2) Isso equivale a 'str | None' (sintaxe disponível no Python 3.10+):


3) Optional não torna o valor automaticamente opcional nem define um 
   valor padrão. Apenas descreve os valores permitidos. 
'''

@dataclass
class Usuario:
    # O SQLite preenche o ID ao cadastrar. Antes disso, ele é 'None'.
    id: Optional[int] = None

    # Valores padrão permitem criar o objeto sem informar todos os campos.
    nome: str = ""

    # A data é armazenada como texto no formato AAAA-MM-DD neste exemplo.
    nascimento: Optional[str] = None

'''
OBS:

@dataclass 

1) É um decorador da biblioteca padrão 'dataclasses'. 

2) Ele gera automaticamente métodos comuns para uma classe, principalmente
  __init__ (construtor), __repr__ (representação) e __eq__ (comparação), com 
  base nos atributos anotados.

3) Com isso, você pode criar e exibir um usuário assim:

from dataclasses import dataclass

@dataclass
class Usuario:
    nome: str
    idade: int

usuario = Usuario("Ana", 25)
print(usuario)  # Usuario(nome='Ana', idade=25)

4) Ou seja: @dataclass reduz o código necessário para criar classes 
   que servem principalmente para armazenar dados.
'''