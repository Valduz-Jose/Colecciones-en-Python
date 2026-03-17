# Diccionarios: es una coleccion de datos ordenados y se almacenan en forma de llave:valor. Se definen utilizando llaves {} y cada elemento se representa como una pareja de clave:valor. Los diccionarios son útiles para almacenar datos relacionados y acceder a ellos mediante sus claves.
print("****** Manejo de Diccionarios ******")

# crear un diccionario
persona = {
  'nombre': 'Sergio',
  'edad':30,
  'ciudad':'Rubio'
}
# no soportan valores duplicados pero si claves duplicadas, en ese caso se toma el ultimo valor asignado a esa clave

print(f"Diccionario Original : {persona}")
# acceder a un valor mediante su clave
print(f"Nombre: {persona['nombre']}")
print(f"Edad: {persona.get('edad')}")
print(f"Ciudad: {persona.get('ciudad')}")

# Modificar el valor de un diccionario
persona['edad'] = 31
print(f"Diccionario Modificado : {persona}")

# agregar un nuevo elemento
persona['profesion'] = 'Ingeniero'
print(f"Diccionario Modificado : {persona}")

# eliminar un elemento
del persona['ciudad']
print(f"Diccionario Modificado : {persona}")

# usndo pop
persona.pop('profesion')
print(f"Diccionario Modificado : {persona}")

# iterar los elementos
print("Iterando sobre el diccionario:")
for clave, valor in persona.items():
    print(f"{clave}: {valor}")
    
# metodo values y metodo keys
print("\n Valores del diccionario:")
for valor in persona.values():
    print(f"Valor: {valor}")
    
print("\n Llaves del diccionario:")
for llave in persona.keys():
    print(f"llave: {llave}")