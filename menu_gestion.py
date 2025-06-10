

print('########## GESTIONAR CLIENTES ##########')
def menu_gestion():
    option: int = input('INGRESE UNA OPCION: \n1. CREAR CLIENTE\n2. AÑADIR PRODUCTOS\n3. VER PRODUCTOS\n4. VER CLIENTES\n5. Eliminar usuario\n')

    if option == '1':
        print('ingresaste opción 1')
    elif option == '2':
        print('ingresaste opción 2')
    elif option == '3':
        print('ingresaste opción 3')
    elif option == '4':
        print('ingresaste opción 4')
    elif option == '5':
        from users import users
        user = users("", "", "", "", "")
        user.remove_user()
    elif option == '6':
        print('Saliendo del sistema...')
        from sistema import run_sistem  
        run_sistem()
        exit()
    





