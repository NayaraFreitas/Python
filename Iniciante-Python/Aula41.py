"""while / else - e possivel usar else no while""" 

string = 'valor qualquer'

i = 0

while i < len(string):
    letra = string[i]

    if letra == ' ':
        break  # toda vez que tiver o break o else não vai ser executado // ,as  se tirar o espaço que esta em string o else e executado


    print(letra)
    i += 1
else:
    print('O else foi executado.')

print('fora do while')