# Conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converte um tipo em outro
#  tipo imutáveis e primitivos:
# str, int, float, bool

print(int('1'),type(int('1'))) # usando afunção int() para fazer coersão do str para int

print(type(float('1.2') + 1)) # função float()
print(bool(''))  #**str vazida = false , strn com espaço true**

print(str(11) + 'b')