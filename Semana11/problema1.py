alumnos={
    'alumno1':'Fernando Sanchez',
    'alumno2':'Carla Gomez',
    'alumno3':'Andrea Fernandez',
    'alumno4':'Martín Martinez',
    'alumno5':'Rosa Pongo',
}
print(alumnos)
print(len(alumnos))
print(alumnos.keys())
print(alumnos.values())
print(alumnos['alumno1'])
print("*"*30)
for key in alumnos.keys():
    print(alumnos[key])
print("*"*30)
alumnos['alumno6'] = 'Lucas Solano'
alumnos_nuevos = {
    'alumno7': 'Carla Ferndez'
}
alumnos.update(alumnos_nuevos)
print("*"*30)
print(alumnos)
del alumnos['alumno6']
alumnos_copy = alumnos.copy()
alumnos.clear()
print("*"*30)
print(alumnos)
print("alumnos_copy")
print("* "*30)
print(alumnos_copy)
print(alumnos_copy.items())
print("* "*30)
print(alumnos_nuevos)
