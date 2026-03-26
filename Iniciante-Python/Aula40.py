# Calculadora com While




while True:
    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite outro numero: ')
    operador = input('Digite um operador (exp.: + - / *):  ')

    numero_validos= None
    numero_1_float = 0
    numero_2_float = 0
    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numero_validos = True

    except:
        numero_validos = None

    if numero_validos is None:
          print('Um ou ambos número digitados são inválidos.')  
          continue
    
    operares_permitidos = '+-/*'

    if operador  not in operares_permitidos:
        print('Operador inválido')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador')
        continue

    print('Resultado ⬇')
    #### 
    if operador == '+':
        print(f'{numero_1_float} + { numero_2_float} =', numero_1_float + numero_2_float)
    elif operador == '-':
        print(f'{numero_1_float} - { numero_2_float} =', numero_1_float - numero_2_float)
    elif operador == '*':
        print(f'{numero_1_float} * { numero_2_float} =', numero_1_float * numero_2_float)
    elif operador == '/':
        print(f'{numero_1_float} / s{ numero_2_float} =', numero_1_float / numero_2_float)    
    else:
        print('Nunca deveria chegar aqui❗')                


    ###
    sair = input('Quer sair? [s]Sim ').lower().startswith('s')
    if sair is True:
        break
    print(sair)    
