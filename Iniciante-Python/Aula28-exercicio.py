"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:

    Exiba:
    Seu nome é {nome}
    Seu nome invertido é {nome invertido}
    Se nome contem(ou não ) espaços
    Seu nome tem (n) Letras
    A primeira letra do seu nome é [letra]
    A última letra do seu nome é [letra]
Se nada for digitado em nome ou idade:
exiba "Desculpe, você deixou campos vazios
 """

nome = input('Digite seu nome: ')
idade = input('Digite sua idade:')
# espaços = nome.count(' ')

if nome and idade:
    print(f'Seu nome é: {nome} \n'
          f'Sua idade é: {idade} \n'
          f'Seu nome invertido: {nome[::-1]} \n'
          f'Seu nome tem {len(nome)} caracteres \n'
          f'A primeira letra do seu nome é:{nome[0]} \n'
          f'A ultima letra do seu nome é: {nome[-1:]}'
         )
    if ' ' in nome:
        print('Seu nome TEM espaços')
    else:
        print('Seu nome NÃO contem espaços')
else:
    print('Desculpe, você deixou os campos vazios')