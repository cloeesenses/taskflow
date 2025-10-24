class Gato:
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self.edad = edad
        self.maullidos = 0

    def presentarse(self):
        print(
            f"Hola!, mi nombre es {self._nombre} y soy un gato de {self.edad} años.")

    def maullar(self):
        self.maullidos += 1
        print(f"{self._nombre} está maullando")
        print(f"{self._nombre} a maullado {self.maullidos} veces")
        return self.maullidos


Salem = Gato("Salem", 5)

Salem.presentarse()
Salem.maullar()
Salem.maullar()
Salem.maullar()
Salem.maullar()
Salem.maullar()
