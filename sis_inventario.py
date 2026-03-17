# programa para gestionar un almacen, usar una lista para mantener un registro de los productos y un diccionario para almacenar los detalles de cada producto, como su id, nombre, cantidad y precio.

print("****** Inventario de Almacen ******")

# crear lista para almacenar los productos
inventario = []
cantidad_productos = int(input("¿Cuántos productos desea agregar al inventario? "))

for i in range(cantidad_productos):
    
    nombre_producto = input(f"Ingrese el nombre del producto {i+1}: ")
    cantidad_producto = int(input(f"Ingrese la cantidad del producto {i+1}: "))
    precio_producto = float(input(f"Ingrese el precio del producto {i+1}: "))
    
    producto = {
        'id': i+1,
        'nombre': nombre_producto,
        'cantidad': cantidad_producto,
        'precio': precio_producto
    }
    # agregar el producto al inventario
    inventario.append(producto)
    
# Mostrar el inventario inicial
print(f'\nInventario inicial: {inventario}')

# buscar un producto por id
id_buscar = int(input("\nIngrese el ID del producto que desea buscar: "))
producto_encontrado = None
for producto in inventario:
    if producto['id'] == id_buscar:
        producto_encontrado = producto
        break

if producto_encontrado is not None:
    print(f"\nProducto encontrado: {producto_encontrado}")
else:
    print(f"\nProducto con ID {id_buscar} no encontrado.")
    
# Mostar el inventario detallado
print("\nInventario detallado:\n\n")
for producto in inventario:
    print(f"ID: {producto['id']}")
    print(f"Nombre: {producto['nombre']}")
    print(f"Cantidad: {producto['cantidad']}")
    print(f"Precio: ${producto['precio']:.2f}")
    print("-"*20)