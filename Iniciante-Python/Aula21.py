# Operadores Lógicos
# and (e) or (ou) not (não)
# AND - Todas as condições precisam ser verdadeiras 
# Se qualquer valor for considerado falso, a expressão intera será avaliada naquele valor falso
# São considerados falsy (que você ja viu)
# Considerados false  = 0 / 0.0 / '' 
# Também existe o tipo None que é usado para representar um não valor "False"
# 

#AND
"""
entrada = input('[E]ntrar [S]air: ')
senha_digita = input('Senha:')

senha_permitida = '123456'


if entrada == 'E' and senha_digita == senha_permitida:
    print('Entrar')
else:
    print('Sair')
"""

#Avaliação de curto circuito
print(True and False and True)
print(True and 0 and True)

print(bool(' '))  # string vazia false , se tiver um espaço dentro é true