#Cuenta regresiva 
def cuenta_regresiva(entrada):
	lista = []
	for i in range (entrada, 0, -1):
		lista.append(i)
	return lista
resultado = cuenta_regresiva(5)
print(resultado)  

#Imprimir y devolver 
def function(lista):
	for num in lista:
		print(lista[0])
		return lista[1]
x = function([1,2])
print(x)

#Primero mas longitud 
def longitud(lista_1):
	sum = lista_1[0] + len(lista_1)
	return sum 
print(longitud([1,2,3,4,5])) 

#Valores mayores que el segundo 
def mayor_segundo(entrada):
	lista_2 = []
	count = 0
	for i in entrada:
		if i > entrada[1]:
			lista_2.append(i)
			count =+ count
		else: 
			print(i)
	print(count)
	return lista_2
resultado = mayor_segundo([5,2,3,2,1,4])
print(resultado)

#Esta longitud, ese valor
def long_valor(longitud, valor):
    lista_3 = []
    for j in range(longitud):
        lista_3.append(valor)
        return lista_3
resl = long_valor(4, 7)
print(resl)