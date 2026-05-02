"""
Faça um jogo para o usuário adivinhar qual a palavra secreta.

Você vai propor uma palavra secreta qualquer e vai dar a possibilidade parao usuário digitar apenas uma letra.
Qual o usuário digitar uma letra, você vai conferir se a letra digitada está na palavra secreta.
    - Se a letra digitada estiver na palavra secreta : exiba a letra ;
    - Se a letra digitada não estiver na palvra secreta ; exiba *.
Faça a contagem de tentativas do seu usuário
"""

#Minha tentaiva
"""
print('Jogo do Adivinhe a Palavra 🧩')
letra_digitada = input('Digite uma letra: ')
palavra_secreta = 'perfume'

for letra in letra_digitada:
    pegando_cada_letra_da_palavra_secreta = len(palavra_secreta)

    if letra == pegando_cada_letra_da_palavra_secreta:
        print(f'')
"""

#import os

palavra_secreta = 'perfume'
letras_acertadas = ''
numeros_tentativas = 0

print('Jogo de Adivinhar a palavra secreta')
while True:
    letra_digitada = input('Digite uma letra: ')
    numeros_tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
            palavra_formada += letra_secreta
        else:
            palavra_formada += '*'

    print(f'Palavra formada = {palavra_formada}')

    if palavra_formada == palavra_secreta:
        print('Você acertou ! Parabens!')
        print(f'Tentativas = {numeros_tentativas}')
        letras_acertadas = ''
        numeros_tentativas = 0
   