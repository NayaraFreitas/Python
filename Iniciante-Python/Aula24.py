# Operadores in e not in
# Strings são iteráveis - (navegar item por item utilizado os  indices)
# 0 1 2 3 4 5
# O t á v i o
#-6-5-4-3-2-1

# nome = 'Nayara'
"""print(nome[2]) #utilzando o dois para idenficar a letra pelo indece
print(nome[-4])"""

"""
print('y' in nome) # true
print('z' in nome) # false

print('y' not in nome) #false
print('z' not in nome) # true
"""
nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')
