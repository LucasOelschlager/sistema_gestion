def run_sistem ():
    print("Sistema iniciado...")
    user_ok = False
    option = int (input("Ingrese una opción: \n1. Crear usuario\n2. Iniciar Sesion\n "))
    if option == 1:
            from users import users
            usuario = users("", "", "", "", "")
            usuario.create_user()
    elif option == 2:
            user_ok = True
            print("Iniciando sesión...")

    else:
            print("Opción no válida. Inténtelo de nuevo.")
            run_sistem()  # Llamar a la función nuevamente para permitir otra entrad\
run_sistem()  # Iniciar el sistema al ejecutar el script