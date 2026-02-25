# função print() dentro dela usa os argumentos (nomeado e não nomeados){como por sep="" que é um separador}

print(12,74, sep= '-' , end="## \n") # se eu tira o \n  ele ira juntar os dois prints , normalmente como possuio u crlf por conta do windows ele ja separa as linhas 
print(56,74, sep= '*' )

# \r\n = CRLF -Padrão Windows. Move o cursor para o início da linha e, em seguida, para a linha de baixo
# \n =LF - Padrão Unix/Linux/macOS moderno. Move o cursor apenas para a linha de baixo.