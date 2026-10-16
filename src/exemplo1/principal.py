# principal.py

import modulo

print(modulo.__name__)  # Imprime "modulo".
print(__name__)         # Imprime "__main__".

"""
1) '__name__' em 'principal.py' se refere ao próprio arquivo atual. 

2) 'modulo.__name__' acessa o valor de '__name__' no módulo importado. 

3) Se 'modulo.py' for executado diretamente, seu '__name__' será "__main__":

python modulo.py 
__main__

4) Se 'modulo.py' for importado, seu '__name__' será o nome do módulo:

python principal.py
modulo
modulo
__main__

"""