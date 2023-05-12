from abc import ABC, abstractmethod

class InstrumentoEscritura(ABC):
    def __init__(self, nombre, marca, modelo, color, tinta):
        self.nombre = nombre
        self.marca = marca
        self.modelo = modelo
        self.color = color
        self.tinta = tinta

    @abstractmethod
    def escribir(self):
        pass

class Boligrafo(InstrumentoEscritura):
    def __init__(self, nombre, marca, modelo, color, tinta, punta):
        super().__init__(nombre, marca, modelo, color, tinta)
        self.punta = punta

    def escribir(self):
        return f"Escribiendo con un bolígrafo {self.color} de {self.marca} modelo {self.modelo} con punta de {self.punta}mm y tinta {self.tinta}"

class Lapiz(InstrumentoEscritura):
    def __init__(self, nombre, marca, modelo, color, dureza):
        super().__init__(nombre, marca, modelo, color, None)
        self.dureza = dureza

    def escribir(self):
        return f"Escribiendo con un lápiz {self.color} de {self.marca} modelo {self.modelo} con dureza {self.dureza}"

class Rotulador(InstrumentoEscritura):
    def __init__(self, nombre, marca, modelo, color, punta):
        super().__init__(nombre, marca, modelo, color, None)
        self.punta = punta

    def escribir(self):
        return f"Escribiendo con un rotulador {self.color} de {self.marca} modelo {self.modelo} con punta de {self.punta}mm"