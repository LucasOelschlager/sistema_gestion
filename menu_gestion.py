

print('########## GESTIONAR CLIENTES ##########')
def menu_gestion():
    option: int = input('INGRESE UNA OPCION: \n1. CREAR CLIENTE\n2. AÑADIR PRODUCTOS\n3. VER PRODUCTOS\n4. VER CLIENTES\n5. Eliminar usuario\n6. Gestionar Clientes\n7. Gestionar Productos\n8. Salir\n')

    if option == '1':
       from clientes import clientes
       cliente = clientes('', '', '', '', [])
       cliente.crear_cliente()
       menu_gestion()
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
        print('ingresaste opción 6')
    elif option == '7':
        print('ingresaste opción 7')
    elif option == '8':
        print('Saliendo del sistema...')
        from sistema import run_sistem  
        run_sistem()
        exit()
    





