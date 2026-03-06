primeiro_valor = int(input('Digite um valor: '))
segundo_valor = int(input('Digite um outro valor: '))


if primeiro_valor > segundo_valor:
    print(
          f'{primeiro_valor=} é maior'
          f' que o  {segundo_valor=}'
         )
elif primeiro_valor < segundo_valor:
    print(
          f'{primeiro_valor=} é menor'
          f' ao {segundo_valor=}'
         )
else:
    print(f'{primeiro_valor} é igual {segundo_valor}')
