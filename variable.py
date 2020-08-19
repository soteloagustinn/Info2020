lista = []
lista2 = []
p =  True
while p == True :
	elemento = int(input('Ingrese un numero para la lista \n'))
	elemento2 = elemento**2
	lista.append(elemento)
	lista2.append(elemento2)
	x = int(input('ingrese 1 si quiere seguir y 0 si no \n'))
	if x == 0 :
		p = False
print(lista)
print('lista con su elementos al cuadrado', lista2)
