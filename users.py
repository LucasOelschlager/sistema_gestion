from validaciones.validacionContrasena import validar_contrasena
from validaciones.validacionEmail import validar_email
from validaciones.validacion_nombreApellido import validar_textos
allUsers = []

class users:
    def __init__ (self, user, password, email, name, last_name, user_data):
        self.user = user
        self.password = password
        self.email = email
        self.name = name
        self.last_name = last_name
        self.user_data = user_data
        
    def create_user(self):
        '''EN ESTA SECCION VALIDO NOMBRE DE USUARIO CON FUNCIONES DE PYTHON. NOT INPUT_USER VALIDA QUE SE HAYA INGRESADO ALGO
            LEN(INPUT_USER) VALIDA QUE TENGA AL MENOS 3 CARACTERES, ISSPACE() VALIDA QUE NO SEA SOLO ESPACIOS 
            Y ISALNUM() VALIDA QUE SEA ALFANUMERICO PARA QUE NO SE INGRESEN CARACTERES ESPECIALES
        '''

        print("########## CREAR USUARIO ##########")
        self.user_data = []
        while True:
            input_user = input("Ingrese su nombre de usuario: ")
            if(validar_textos(input_user, 'Usuario')):
                self.user = input_user
                break
        while True:
            nameInput = input('Ingrese su nombre ')
            if(validar_textos(nameInput, 'Nombre')):
                self.name = nameInput
                break
        while True:
            last_nameInput = input('Ingrese su nombre ')
            if(validar_textos(last_nameInput, 'Nombre')):
                self.last_name = last_nameInput
                break
          
        '''EN ESTA SECCION VALIDO EL EMAIL CON UNA FUNCION DE VALIDACION QUE USA UN REGEX'''
       
        while True:
                input_email = input("Ingrese su correo electrónico: ")
                if validar_email(input_email):
                    self.email = input_email
                    break
        ''''EN ESTA SECCION VALIDO CONTRASENA CON FUNCION DE VALIDACION QUE USAR REGEX'''
      
        while True:
            try:
                input_password = input("Ingrese su contraseña: ")
                confirm_password = input("Confirme su contraseña: ")
                if validar_contrasena(input_password, confirm_password):
                    break
            except ValueError:
                print("La contraseña no es válida. Inténtelo de nuevo.")
                input_password = input("Ingrese su contraseña: ")
                confirm_password = input("Confirme su contraseña: ")
        print(f"Usuario creado exitosamente.\nNombre de usuario: {self.user}\nNombre: {self.name}\nApellido: {self.last_name}\nEmail: {self.email}")
        usuario = users(self.user, input_password, self.email, self.name, self.last_name, self.user_data)
        allUsers.append(usuario)
        print(usuario.user, usuario.email, usuario.name, usuario.last_name)
        from sistema import run_sistem
        run_sistem()

    def remove_user(self):
        userRemove = input('Ingrese el usuario a eliminar: ')
        for user in allUsers:
            if user.user == userRemove:
                passwordRemove = input(f'Ingrese la contraseña de {user.user}: ')
                if user.password == passwordRemove:
                    allUsers.remove(user)
                    print(f'Usuario {user.user} eliminado exitosamente.')
                    return
               



        