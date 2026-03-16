# Solicitar cuantas canciones va a agregar a la lista de reproducción

print("*****Playlist de canciones*****")

lista_reproduccion = []
lista_reproduccion.append("Bohemian Rhapsody - Queen")
lista_reproduccion.append("Stairway to Heaven - Led Zeppelin")
lista_reproduccion.append("Hotel California - Eagles")
lista_reproduccion.append("Imagine - John Lennon")

# Ordenar en orden alfabetico
lista_reproduccion.sort()

# mostrar la lista de reproduccion
print(f"Lista de Reproducción : {lista_reproduccion}")

# si lo quisiera ordenar en orden inverso
lista_reproduccion.sort(reverse=True)

# iterando los elementos de la lista de reproduccion
for cancion in lista_reproduccion:
    print(f"{cancion}\n")