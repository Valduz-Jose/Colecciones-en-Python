# Tuplas son como listas pero estas son inmutables, lo que significa que no se pueden modificar después de haberlas creado. ni a*adir mas elementos, ni eliminar, ni modificar los existentes. Se definen utilizando paréntesis () y los elementos se separan por comas.
# mi_tupla = (1, 2, 3, 'hola', True)
# los parentesis son opcionales, por lo que también se puede definir una tupla sin ellos, simplemente separando los elementos por comas.
# mi_tupla = 1, 2, 3, 'hola', True
# existe la tupla unitaria que es una tupla con un solo elemento, para definirla se debe incluir una coma después del elemento.
# tupla_unitaria = (42,)
print("****** Manejo de Tuplas ******")

mi_tupla = (1,2,3,4,5)
print(f"Tupla Original : {mi_tupla}")

# iteramos los elementos
for elemento in mi_tupla:
    print(elemento)
    
# crear una tupla para una coordenada x,y
coordenadas = (3,5)

print(f"\nCoordenada en X: {coordenadas[0]} \nCoordenada en Y: {coordenadas[1]}")

# Tupla unitaria
tupla_un_elemento = 10,
print(f"\nTupla unitaria : {tupla_un_elemento}")

# Tupla anidada

tupla_anidada = (1, 2, (3, 4), 5)
print(f"\nTupla Anidada : {tupla_anidada}")
print(f"Elemento anidado : {tupla_anidada[2][0]}")