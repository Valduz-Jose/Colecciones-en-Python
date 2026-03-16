# Los sets son colecciones de datos no ordenadas y sin elementos duplicados. Se definen utilizando llaves {} o la función set(). Los sets son útiles para almacenar elementos únicos y realizar operaciones de conjunto como unión, intersección y diferencia.

print("****** Manejo de Sets ******")

# crear un conjunto
mi_set = {1,2,3,4,5,4}
# el segundo 4 no se agrega porque los sets no permiten elementos duplicados
print(f"Set Original : {mi_set}")

# agregar elementos a un set 
mi_set.add(6)
mi_set.add(7)
print(f"Set Modificado : {mi_set}")

# intento agregar elemento duplicado
mi_set.add(3)
print(f"Set Modificado : {mi_set}")

# eliminar un elemento
mi_set.remove(4)#elimina ese valor del set
print(f"Set Modificado : {mi_set}")

# iterar un set 
for elemento in mi_set:
    print(elemento, end=" ")
    
# comprobar si existe un elemento en el set 
print(f"\n¿Existe el elemento 5 en el set? {'Sí' if 5 in mi_set else 'No'}")

# obtener la longitud del set 
print(f"Longitud del conjunto: {len(mi_set)}")