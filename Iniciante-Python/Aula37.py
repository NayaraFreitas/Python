"""
While + continue (é uma ferramenta de controle de fluxo para ignorar partes específicas do código com base em uma condição, sem finalizar o laço inteiro. )
"""

contador = 0

while contador <= 100:
    contador += 1 # este linha que controla o while , oe que pode gera um laço infinito

    if contador == 6:
        print('Não vou mostra o 6')
        continue 
    
    if contador >= 10 and contador <= 27:
        print('Não existe do 10 ao 27')
        continue

    print(contador)

    if contador == 40:
        print(contador)
        break


print('Acabou')
