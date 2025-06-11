from validaciones.validacion_nombreApellido import validar_textos

class clientes:
    total_clientes: int = 0
    def __init__ (self, nombre: str, apellido: str, dni: int, razon_social: str, productos: list):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.razon_social = razon_social
        self.productos = productos

    def crear_cliente(self): 
        self.nombre = validar_textos('Nombre')
        self.apellido = validar_textos('Apellido')
        print(f'Nombre: {self.nombre}\nApellido: {self.apellido}')