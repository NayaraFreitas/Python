"""
Explicação de while para contar string , e validar
"""
# texto = 'Python'

# i = 0
# tamanho_string = len(texto)

# while i < tamanho_string:
#     print(texto[i], i)

#     i += 1

"""
While  para saber quantas repetições
"""
# senha_salva = '123456'
# senha_digitada = ''

# repeticoes = 0

# while senha_salva != senha_digitada:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')

#     repeticoes += 1


# print(repeticoes)
# print('Aquele laço acima pode ter repetições infinitas')

"""
For in - mesma iteração que o while faz so que mais simples
"""

texto = 'Python' # uma string é iteravel

novo_texto = ''

for letra in texto:
    novo_texto += f'*{letra}'
    print(letra)

print(novo_texto + '*')