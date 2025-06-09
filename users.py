from validaciones import validacionEmail, validacionContrasena

allUsers = []

class users:
    def __init__ (self, user, password, email, name, last_name):
        self.user = user
        self.password = password
        self.email = email
        self.name = name
        self.last_name = last_name
        
    def create_user(self):
        '''EN ESTA SECCION VALIDO NOMBRE DE USUARIO CON FUNCIONES DE PYTHON. NOT INPUT_USER VALIDA QUE SE HAYA INGRESADO ALGO
            LEN(INPUT_USER) VALIDA QUE TENGA AL MENOS 3 CARACTERES, ISSPACE() VALIDA QUE NO SEA SOLO ESPACIOS 
            Y ISALNUM() VALIDA QUE SEA ALFANUMERICO PARA QUE NO SE INGRESEN CARACTERES ESPECIALES
        '''

        while True:
            input_user = input("Ingrese su nombre de usuario: ")
            if not input_user or len(input_user) < 3 or input_user.isspace() or not input_user.isalnum():
                print("El nombre de usuario debe tener al menos 3 caracteres, no puede estar vacío y debe ser alfanumérico.")
                
            else:
                self.user = input_user
                print(f"usuario {self.user}")
                break

        while True:
            input_name = input("Ingrese su nombre: ")
            if not input_name or len(input_name) < 3 or input_name.isspace() or not input_user.isalnum():
                print("El nombre debe tener al menos 3 caracteres y no puede estar vacío.")
            else:
                self.name = input_name
                break

        while True:
            input_lastName = input("Ingrese su apellido: ")
            if not input_lastName or len(input_lastName) < 3 or input_lastName.isspace():
                print("El apellido debe tener al menos 3 caracteres y no puede estar vacío.")
            else:
                self.last_name = input_lastName
                break
        '''EN ESTA SECCION VALIDO EL EMAIL CON UNA FUNCION DE VALIDACION QUE USA UN REGEX'''
        input_email = input("Ingrese su correo electrónico: ")
        while True:
            try: 
                if validacionEmail.validar_email(input_email):
                    self.email = input_email
                    break
            except ValueError:
                print("El correo electrónico no es válido. Inténtelo de nuevo.")
                input_email = input("Ingrese su correo electrónico: ")

        ''''EN ESTA SECCION VALIDO CONTRASENA CON FUNCION DE VALIDACION QUE USAR REGEX'''
      
        while True:
            try:
                input_password = input("Ingrese su contraseña: ")
                confirm_password = input("Confirme su contraseña: ")
                if validacionContrasena.validar_contrasena(input_password, confirm_password):
                    break
            except ValueError:
                print("La contraseña no es válida. Inténtelo de nuevo.")
                input_password = input("Ingrese su contraseña: ")
                confirm_password = input("Confirme su contraseña: ")
        print(f"Usuario creado exitosamente.\nNombre de usuario: {self.user}\nNombre: {self.name}\nApellido: {self.last_name}\nEmail: {self.email}")


        