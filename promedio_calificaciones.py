print("Promedio Calificaciones")

numero_calificaciones = int(input("¿Cuántas calificaciones deseas ingresar? "))

calificaciones = []
for i in range(numero_calificaciones):
    calificacion = float(input(f"Ingresa la calificación {i+1}: "))
    calificaciones.append(calificacion)

promedio = sum(calificaciones) / len(calificaciones)
print(f"El promedio de las calificaciones es: {promedio}")