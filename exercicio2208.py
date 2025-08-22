# classe boneca

class Boneca:
    def __init__(self, modelo, marca, preco, material):
        self.modelo = modelo
        self.marca = marca
        self.__preco = preco
        self.__material = material

    def __str__(self):
        return f"{self.modelo}\n - {self.marca}\n - {self.__preco}\n - {self.__material}\n"

Boneca1 = Boneca("Monster High", "Mattel", 230, "Plástico")
print(Boneca1)

Boneca2 = Boneca("Barbie", "Mattel", 120, "plástico")
print(Boneca2)
