# crear una agenda de contactos usando diccionarios
print("Agenda de Contactos")
agenda = {
  'Carlos':{
    'telefono': '123456789',
    'email': 'carlos@gmail.com',
    'direccion': 'Calle Principal'
  },
  'Maria':{
    'telefono': '998898152',
    'email': 'maria@gmail.com',
    'direccion': 'Calle tercera'
  },
  'Pedro':{
    'telefono': '626215165',
    'email': 'pedro@gmail.com',
    'direccion': 'Calle segunda'
  }
}

print(f"Agenda Original:\n {agenda}")

# acceder a la info de un contacto especifico
print(f'''
      Info de Carlos:
      Teléfono: {agenda['Carlos']['telefono']}
      Email: {agenda['Carlos']['email']}
      Dirección: {agenda.get('Carlos').get('direccion')}
      ''')

# agregar un nuevo contacto
agenda['Ana']={
  'telefono': '245215555',
  'email':'ana@gmail.com',
  'direccion': 'Calle cuarta'
}

print(f"Agenda Modificada:\n {agenda}")

# eliminiar un contacto
agenda.pop('Pedro')
del agenda['Maria']
print(f"Agenda Modificada:\n {agenda}")

# mostramos los contactos
for nombre, detalles in agenda.items():
  print(f'''Nombre: {nombre}
        Telefono: {detalles.get('telefono')}
        Email: {detalles.get('email')}
        Direccion: {detalles.get('direccion')}
        ''')
