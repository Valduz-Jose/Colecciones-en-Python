# Listas y tuplas combinadas
print("**** Combinacion de Listas y Tuplas ****")
# defino una lista q almacena tuplas de productos

productos = [
  ("P001","Camiseta",20.00),
  ("P002","Jeans",30.00),
  ("P003","Sudadera",40.00),
]
# imprimir la info de cada producto y calcular el precio total 
precio_total = 0;
print("Lista de Productos:")
for producto in productos:
  # unpacking de la tupla producto
    id, descripcion, precio = producto
    print(f"ID: {id}, Descripción: {descripcion}, Precio: ${precio:.2f}")
    precio_total += precio
print(f"Precio Total: ${precio_total:.2f}")