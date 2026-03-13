"""
https://docs.python.org/pt-br/3/library/stdtypes.html
Imutáveis que vimos: str, int, float, bool
"""
string = 'luiz Otavio'
#outra_varial = string
#string[3] = 'ABC' # não é possivel fazer isso no python pois str e imutavel

#  se for mudar tem que colocar em outra variavel, gerando um nova variavel
# outra_variavel = f'{string[:3]}ABC{string[4:]}' 
# print(string)
# print(outra_variavel)
# print(string.capitalize()) # vai pegar a primeira letra minuscula em maiuscula

print(string.zfill(100)) # adiciona mais caracteres



