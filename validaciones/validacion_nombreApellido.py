def validar_textos(campo, tipo_campo) -> str:
     while True:
            if(not campo or len(campo) < 3 or campo.isspace() or not campo.isalnum()):
                print(f'Error: El {tipo_campo} no debe estar vacio, debe tener al menos 3 letras y no debe tener espacios')
                return False
            else:
                return campo
            
            
            