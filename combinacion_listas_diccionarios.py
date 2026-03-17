# 
print("Combinacion de Listas y Diccionarios")

personas = [
  {
    'nombre':'Regina',
    'apellido':'Flores',
    'edad':21
    },
  {
    'nombre':'Alejandro',
    'apellido':'Reyes',
    'edad':25
  }
]

print(f"Lista de personas: {personas}")

# acceder a un diccionarfio desde una lista
print(f'''
      \n
      Nombre: {personas[0].get('nombre')}
      Apellido: {personas[0].get('apellido')}
      Edad: {personas[0].get('edad')}
      \n
      Nombre: {personas[1].get('nombre')}
      Apellido: {personas[1].get('apellido')}
      Edad: {personas[1].get('edad')}
      ''')

# recorrer los elementos de la lista y acceder a los diccionarios
for contador, persona in enumerate(personas):
  print(f'{contador+1} - Persona: {persona}')
  