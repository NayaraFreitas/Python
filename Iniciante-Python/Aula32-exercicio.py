"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou impar. Caso o usuário não digite um número interiro, informe que não é um número inteiro.
"""
# print('Informe um número para saber se é impar ou par')
# numero = int(input('Digite um número:'))

# if numero % 2 == 0:
#     print(f'O número {numero} é par')
# else:
#     print(f'O número {numero} é impar')

""" Solução do Professor"""
#if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'ímpar'

#     if par_impar:
#        par_impar_texto = 'par'
#        print(f'O número {entrada_int} é {par_impar_texto}') 

# else:
#     print('Você não digitou um número inteiro')


# entrada = input('Digite um número: ')

# try:
#     entrada_int = float(entrada)
#     par_impar = entrada_int % 2 == 0
#     par_impar_texto = 'impar'

#     if par_impar:
#       par_impar_texto = 'par'
#       print(f'O número {entrada_int} é {par_impar_texto}')
    
# except:
#      print('Vocè não digitou un número inteiro')




"""
Faça um progrma que pergunte a hora ao usuário e, baseando-se no horário  descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23 
"""

# from datetime import datetime

# print('Qual o horário agora')
# horario = input('Digite seu horario hh:mm: ')

# try:
#     hora_obj = datetime.strptime(horario, "%H:%M")
#     hora = hora_obj.hour

#     if hora <= 11 :
#          print('Bom dia')
#     elif hora <= 17:
#          print('Boa tarde')
#     else:
#          print('Boa noite')
# except:
#      print('Formato incorreto')


"""
Faça um progrma que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou menos escreve "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

""" Minha solução"""
# print('Vamos saber se seu nome é curto!')
# nome = input('Digite seu primeiro nome: ')

# if len(nome) >= 6:
#      print('Seu nome é muito grande')
# elif 5 <= len(nome) <= 6:
#      print('Seu nome é normal')
# else:
#      print('Seu nome é muito curto')

""" Versão melhorada"""
# print('Vamos saber se seu nome é curto!')
# nome = input('Digite seu primeiro nome: ')
# tamanho = len(nome)

# # evite usar muitas vezes o len  e tambem pense do menor para o maior quando usa if elif else
# if tamanho <= 4:
#     print('Seu nome é muito curto')
# elif tamanho <= 6:
#       print('Seu nome é normal')
# else:
#      print('Seu nome é muito grande')

""" versão professor"""
nome = input('Digite seu primeiro nome: ')
tamanho = len(nome)

if tamanho > 1:
     if tamanho <= 4:
       print('Seu nome é muito curto')
     elif tamanho >= 5 and tamanho <= 6:
        print('Seu nome é normal')
     else:
           print('Seu nome é muito grande')
else:
     print('Digite mais de uma letra')