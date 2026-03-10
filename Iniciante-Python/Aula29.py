"""
Introdução ao try/except (try/catch em outras linguagens)
try --> tentar executar o código
execpt -> ocorreu algum erro ao tentar executar
"""

numero_str = input('Vou dobrar o número que você digitar:')

 #.isdigit ele tem função de sabe se o usuario digita so numeros
# if numero_str.isdigit():                                        #"If seja condição e muda o fluxo"
#     numero_float = float(numero_str)
#     print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
# else:
#     print('Isso não é um número')

#  Se ocorrer um erro e melhor usar try/execpt - o if não evita execeções

try:
    print('STR :' , numero_str)
    numero_float = float(numero_str)
    print('FLOAT :', numero_float)
    print(f'O dobro de {numero_str} é {numero_float * 2:.2f}')
except:
    print('Isso não é um número')
