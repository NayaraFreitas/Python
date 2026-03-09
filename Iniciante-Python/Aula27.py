"""
Fatiamento de strings
 012345678
 olá mundo
-987654321
Fatiamento [i:f:p] [::] # i=inicio , f=fim , p=pular
Obs.: a função len retorna a qtd
de caracteres de str
"""

variavel = 'Olá mundo'
#print(len(variavel[4:])) # os : que indica o fatiamento se deixa [0:] se omitir o final e para pegar o final todo, [:0]se omitir o começa e para pegar o começo todo
#len e mesma coisa  de lenght , so funciona melhor em str

print(variavel[::-1]) # a str fica invertida