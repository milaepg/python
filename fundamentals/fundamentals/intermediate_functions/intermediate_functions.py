#Actualizar valores en diccionarios y listas
x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ] 
#1.-
def xChanger(x):
    for el in x:
        for i, n in enumerate(el):
            if n == 10:
                el[i] = 15
    return x

estudiantes[0]['last_name'] = 'Bryant'
 
directorio_deportes['fútbol'][0] = 'Andres'
 
z[0]['x'] = 500
#Iterar a través de una lista de diccionarios
estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(data_entrada):
    for iterador in data_entrada:   
        valor = list(iterador.items())
        print(valor[0][0]," - ", valor[0][1], ",", valor[1][0]," - ", valor[1][1])
iterateDictionary(estudiantes)

#Obtener valores de una lista de diccionarios
def iterateDictionary2(key_name, some_list):
    if key_name in some_list:
        print(some_list[key_name])
    else:
        if isinstance(some_list[0], dict):
            for iterador in some_list:
                print(iterador[key_name])
        else:
            print("Error, no existe el indice ingresado")

#Obtner primer nombre
iterateDictionary2("first_name", estudiantes)
print('-------------------------------------------------------------------')
#Obtner Segundo nombre
iterateDictionary2("last_name", estudiantes)
print('-------------------------------------------------------------------')
#Obtner directorio de deportes
iterateDictionary2("basketball", directorio_deportes)

#Iterar a través de un diccionarios con valores de lista
dojo = {
   'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
   'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
def printInfo(some_dict):
    for listas in some_dict:
        print(len(some_dict[listas]), listas)
        for x in some_dict[listas]:
            print(x)
        print(" ")
printInfo(dojo)
