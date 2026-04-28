""""
Iterável -> str , range, etc (__iter__) - entrega um elemento por vez
Iterador -> quem sabe entregar um valor por vez
next -> me entregue o proximo valor - quando acaba os valores ele mostra um erro
iter -> me entregue seu iterador

"""
"""
# texto = iter('Nayara') #.__iter__()
# print(next(texto)) #.__next__()
"""


texto = 'Luiz' #iteravel
iteratador = iter(texto) #iterator

# fazendo um laço usando o next dentro e usando o try e execpt para tratar o error para quando acabar os valores, ai deposi que trata ele da um break e termina o laço
while True:
    try:
        print(next(iteratador))
    except StopIteration:
        break


# isso e a mesma coisa que o de  cima , ou seja o de cima e uma explicanção do que acontece por de baixo dos panos no for in
for letra in texto:
    print(letra)