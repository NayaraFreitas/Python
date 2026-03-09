"""
Formatação básica de strings
s - string
d - int
f - float
.<número de digitos>f
x ou X Hexadeciaml
(carcterer)(><^)(qantidade)
> esquerda
< Direita
^ Centro
= - Força o número a aparecer antes dos zeros
Sinal + ou -
Ex.: 0>-100,.1f
Conversion flags  - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}') #usando o > para direceionar o lado para adicionar 10 espaço
print(f'{variavel: <10}.') #usando o < para direceionar o lado para adicionar 10 espaço
print(f'{variavel:0^10}.') 
print(f'{1000.487361849849:0=+10,.1f}') 
print(f'O hexadecimal de %d é %04X {1500:08X}')
print(f'{variavel!r}')

