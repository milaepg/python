num1 = 42 # variable con numero clase int 
num2 = 2.3 # variable con numero clase float 
boolean = True # variable booleana 
string = 'Hello World' # variable tipo string 
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # lista que contiene 5 elementos string
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable tipo diccionario
fruit = ('blueberry', 'strawberry', 'banana') # variable que almacena dato tipo tupla
print(type(fruit))  # imprime en pantalla y type devuelve el tipo de variable que en este caso es tupla
print(pizza_toppings[1]) #imprime el elemnto de la posición 1 que es Sausage.
pizza_toppings.append('Mushrooms') # Agrega a la lista Mudhrooms
print(person['name']) #muestra en pantalla John
person['name'] = 'George' # Cambia el elemento John por George
person['eye_color'] = 'blue' # agrega a la person el elemento "eye_color"
print(fruit[2]) # imprime banana
"""Si num1 es mayor a 45 imprime: It's greater. 
Si la sentencia if la evalua como False pasa a la siguiete sentecia e imprime: It's lower """
if num1 > 45:
    print("It's greater")
else:
    print("It's lower")

"""Si el largo de la varieble string es menor a  5 imprime: It's a short word!"""
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15: #Si la sentencia anterior es falsa, se imprime: It's a long word!, si el largo de la variable string es mayor a 15.
    print("It's a long word!")
else: #Si las sentencias if y elif no se cumplen, muestra en pantalla: Just right!
    print("Just right!")

for x in range(5):
    print(x) # imprime 0 1 2 3 4
for x in range(2,5): 
    print(x) # imprime 2 3 4
for x in range(2,10,3):
    print(x) # imprime 2 5 8 
x = 0
while(x < 5):
    print(x) # imprime 0 1 2 3 4
    x += 1

pizza_toppings.pop() # elimina el ultimo elemento del array, que seria Mushrooms 
pizza_toppings.pop(1) # elimina Suasage

print(person) #imprime 'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False, 'eye_color': 'blue'
person.pop('eye_color') # remueve el string 
print(person) # imprime 'name': 'George', 'location': 'Salt Lake', 'age': 37, 'is_balding': False

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')# imprime 10 veces Hello

print_hello_ten_times()

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')# imprime 4 veces Hello

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')# Imprime 14 veces Hello 

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)