from unittest import result

#Recursividad en Programación Funcional 
def fibonacci(posicion):
    if posicion > 1:
        return fibonacci(posicion-1) + fibonacci(posicion-2)
    return posicion

resultado = fibonacci(6)
print("El resultado de la sucesión de fibonacci en la posición 6 es: ",resultado)

def fibonacci_iter(n):
    a=1
    b=1
    if n==1: 
        print('0')
    elif n==2:
        print('0','1')
    else:
        print('0')
        print(a)
        print(b)
        for i in range(n-3):
            total = a + b
            b=a
            a= total
            print(total)


#Funciones Puras
precio=120000

def funcion_pura(precio, cantidad):
    return (precio*cantidad)

def funcion_no_pura(cantidad):
    global precio
    precio=precio*cantidad
    return precio


print("Esta es una función pura: ")
print(funcion_pura(precio,3))
print("Variable global precio")
print(precio)

print("Esta no es una función pura")
print(funcion_no_pura(3))
print("Variable global precio")
print(precio)

#Inferencia de tipos
#Orden Superior
def doble(x):
    return x+x

def cuadruple(x):
    return doble(x)+doble(x)

print("El cuadruple de 2 es: ")
print(cuadruple(2))


#Funciones Lambda
mi_lista = [1, 2, 3, 4, 5, 6]
print(mi_lista)
lista_nueva = list(map(lambda x: x * 2, mi_lista))
print(lista_nueva)  # [2, 4, 6, 8, 10, 12]