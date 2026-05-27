# Cree una clase de Python llamada Usuario que use el método init 
# y cree un nombre de usuario y una contraseña. 
# Crea un objeto usando la clase.


class Usuario:
    def __init__(self, usuario, contraseña):
        self.usuario = usuario
        self.contraseña = contraseña
    

usuario1 = Usuario('Martin11', 'clarinete')        