# Son coleeciones ordenadas y mutables de elementos, que pueden contener elementos de diferentes tipos.
# Se definen utilizando corchetes [] y los elementos se separan por comas.
# mi_lista = [1, 2, 3, 'hola', True]
# Las listas pueden contener elementos de diferentes tipos, incluyendo otras listas.

# Las listas son mutables, lo que significa que puedes modificar sus elementos después de haberlas creado.
print("Manejo de Listas")

mi_lista = [1,2,3,4,5]

print(f"Lista Original : {mi_lista}")
print(f"Largo de la Lista : {len(mi_lista)}")

# acceder por indice
print(f"cuarto Elemento : {mi_lista[4]}")
# Se pueden usar indices negativos para acceder a los elementos desde el final de la lista.
print(f"tercer Elemento : {mi_lista[-3]}")