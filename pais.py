class Pais:
    def __init__(self, nombre, confirmados, muertos,recuperados):
        
        self.nombre=nombre
        self.confirmados=confirmados
        self.muertos=muertos
        self.recuperados=recuperados

    def mostrar(self):
        return f'Pais:{self.nombre}, Enfermos:{self.confirmados}, Muertos:{self.muertos}, Recuperados:{self.recuperados}'
    def recuperado(self):
        return f'Pais:{self.nombre} ,Recuperados:{self.recuperados}'
    def muerto(self):
        return f'Pais:{self.nombre}, Muertos:{self.muertos},'
    def confirmado(self):
        return f'Pais:{self.nombre}, Enfermos:{self.confirmados}'