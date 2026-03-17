# Lista de suscriptores
print("****** Lista de Suscriptores ******")
suscriptores = set() #asi se define un set vacio

numero_suscriptores = int(input("Ingrese el número de suscriptores a agregar: "))

for _ in range(numero_suscriptores):
    correo = input(f"Ingrese el correo del suscriptor {_+1}: ")
    suscriptores.add(correo)

print(f"Lista de suscriptores: {suscriptores}")
nuevo_suscriptor = input("Ingrese el correo del nuevo suscriptor: ")

if nuevo_suscriptor in suscriptores:
    print(f"El correo {nuevo_suscriptor} ya está suscrito.")
else:
  suscriptores.add(nuevo_suscriptor)
  print(f"Correo {nuevo_suscriptor} agregado a la lista de suscriptores.")
  
print(f"Lista de suscriptores: {suscriptores}")

# Eliminar un suscriptor
suscriptor_eliminar = input("Ingrese el correo del suscriptor a eliminar: ")

suscriptores.remove(suscriptor_eliminar)
print(f"Correo {suscriptor_eliminar} eliminado de la lista de suscriptores.")

# cantidad total de suscriptores
print(f"Cantidad total de suscriptores: {len(suscriptores)}")
print(f"Lista de suscriptores: {suscriptores}")

# iterar sobre la lista de suscriptores
print("Iterando sobre la lista de suscriptores:")
for correo in suscriptores:
    print(correo)