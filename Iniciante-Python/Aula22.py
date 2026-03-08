# Operador Lógico 
# OR - Qualquer condição avaliada como verdadeira toda a expresão será verdadeira
# 

"""
entrada = input('[E]ntrar [S]air: ')
senha_digita = input('Senha:')

senha_permitida = '123456'

# por ter or e and a expressão pode ficar ambigua
if (entrada == 'E' or entrada =='e') and senha_digita == senha_permitida: # colocar em parentes para ser avaliado primeiro
    print('Entrar')
else:
    print('Sair')
"""

"""print(False or 0 or  0 or 'abc' or True)""" # o primeiro que ele achar verdadeiro ele vai retorner

senha = input('Senha: ') or 'Sem senha' # e possivel usar o operador lógico na variavel
print(senha)