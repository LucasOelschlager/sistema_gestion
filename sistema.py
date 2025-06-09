from menu_gestion import menu_gestion

def run_sistem():
        print("Sistema iniciado...")
        print('----------GESTION DE PRODUCTOS POR CLIENTE----------')
        option = int (input("Ingrese una opción: \n1. Crear usuario\n2. Iniciar Sesion\n3. Salir \n"))
        if option == 1:
                from users import users
                usuario = users("", "", "", "", "")
                usuario.create_user()
        elif option == 2:
                print("Iniciando sesión...")
                menu_gestion()

        elif option == 3:
                print("Saliendo del sistema...")
                exit()
        else:
                print("Opción no válida. Inténtelo de nuevo.")
                run_sistem()  
run_sistem()  