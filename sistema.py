from menu_gestion import menu_gestion
import os



def run_sistem():
       
        print("Sistema iniciado...")
        print('----------GESTION DE PRODUCTOS POR CLIENTE----------')
        option = int (input("Ingrese una opción: \n1. Crear usuario\n2. Iniciar Sesion\n3. Salir \n"))
        if option == 1:
                from users import users
                usuario = users("", "", "", "", "", [])
                usuario.create_user()
        elif option == 2:
                from login import validate_login
                loginOk = validate_login()
                if loginOk:
                        print("Inicio de sesión exitoso.")
                        menu_gestion()
                else: 
                        print("Error en el inicio de sesión. Por favor, intente de nuevo.")
                        run_sistem()
        elif option == 3:
                print("Saliendo del sistema...")
                exit()
        else:
                print("Opción no válida. Inténtelo de nuevo.")
                run_sistem()  
run_sistem()  