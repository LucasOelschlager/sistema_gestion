import re

def validar_email(email):
    patron = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    state = re.match(patron, email) is not None
    if state == False:
        print('El email no es válido, Intente nuevamente')
        return
    else:
        return re.match(patron, email) is not None

    

