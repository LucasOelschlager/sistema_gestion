import re 


def validar_contrasena(contrasena, confirmContrasena):
    patron = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
    if re.match(patron, contrasena) and contrasena == confirmContrasena:
        return True
    else:
        print("La contraseña debe tener al menos 8 caracteres, una letra mayúscula, una letra minúscula, un número y un carácter especial. Además, las contraseñas deben coincidir.")
        return False
