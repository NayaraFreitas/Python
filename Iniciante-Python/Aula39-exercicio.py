"""
Iterando strings com while
"""
      # 01234567891011121314
nome = 'Nayara Freitas' #iteraveis
tamanho_nome = len(nome)
indice = 0
novo_nome = ''
# print(nome)
# print(tamanho_nome)
# print(nome[3])

while indice < tamanho_nome:
    novo_nome += f'*{nome[indice]}'
    indice += 1

novo_nome += '*'

print(novo_nome)