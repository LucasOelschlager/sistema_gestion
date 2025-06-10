from users import allUsers

def validate_login():
    
    print("########## INICIAR SESIÓN ##########")
    if not allUsers:
        print("No hay usuarios registrados. Por favor, cree un usuario primero.")
        return False
    username = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")
    for user in allUsers:
        
        if user.user == username and user.password == password:
            print(f"Bienvenido, {user.name} {user.last_name}!")
        return True