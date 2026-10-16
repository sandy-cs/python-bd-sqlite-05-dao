# principal.py
import modulo

print(modulo.__name__)  # imprime "modulo"

"""
1) '__name__' em 'principal.py' se refere ao próprio arquivo atual. 

2) 'modulo.__name__' acessa o valor de '__name__' no módulo importado. 

3) Se 'modulo.py' for executado diretamente, seu '__name__' será "__main__"; 
   quando importado, será o nome do módulo.
"""