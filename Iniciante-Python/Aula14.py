a = 'A'
b = 'BBBBB' 
c = 1.1

string= 'a={nome1} b={nome2} c={nome3:.2f} ' #:.2f para ter duas casas decimais //  as {} representa o lugar que vai aparacer o resultado  por conta do uso do .format  // se tiver um {} a mais  sem ter uma variaveis correpondente para colocar o dado ira dar um erro // e possivel usar indice dentro , assim não limita a quantidade que deseja que  aparecer(a={0} b={0})
formato = string.format(
    nome1=a, nome2=b, nome3=c
)  
# é possivel nomear os parametros , mas não esqueça de colocar la na variveis esse nome de parametro , senão ira dar KeyError tanto na função quanto na variavel

print(formato)