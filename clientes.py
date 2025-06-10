

class clientes:
    total_clientes: int = 0
    def __init__ (self, id: int, nombre: str, apellido: str, dni: int, razon_social: str, productos: list):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.razon_social = razon_social
        self.productos = productos

    def crear_cliente(self):
        clientes.total_clientes += 1
        self.id = clientes.total_clientes
        print(f'Tu id de cliente es {id}, nombre: Prueba')
 