usuarios = {}

while True:
    email = input("Ingrese un email: ")
    password = input("Password: ")
    if usuarios.get(email) is None:
        usuarios[email] = password
    else:
        print("El email ya existe")

    opcion = input("Desea ingresar otro email? (s/n) ")
    if opcion == "n":
        print("Usuarios registrados: ", usuarios)
        break
    